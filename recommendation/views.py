from collections import Counter
from operator import itemgetter

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views import View

from steam.models import Steam
from .forms import ChooseTagsForm

DEVELOPER_MATCH_SCORE = 15
GENRE_MATCH_SCORE = 50
TAG_MATCH_SCORE = 7


class RecommendGamesManuallyView(View):
    def get(self, request):
        return render(
            request,
            template_name='recommendation/recommendation_preference.html',
            context={'form': ChooseTagsForm().as_p()}
        )

    def post(self, request):
        all_games_qs = Steam.objects.all()
        form = ChooseTagsForm(request.POST)
        if form.is_valid():
            user_genre = form.cleaned_data['genre']
            user_developer = form.cleaned_data['developer']
            user_tags = form.cleaned_data['tags']

            all_games_info = []

            for game in self._assign_matching_tags_to_game(user_tags, all_games_qs):
                game_object = game['game_object']
                game_info = {
                    'game': game_object,
                    'matched_tags': [],
                    'unmatched_tags': []
                }
                match_score = 0

                if game_object.developer == user_developer:
                    game_info['developer_match'] = True
                    match_score += DEVELOPER_MATCH_SCORE
                else:
                    game_info['developer_match'] = False

                if game_object.genre == user_genre:
                    game_info['genre_match'] = True
                    match_score += GENRE_MATCH_SCORE
                else:
                    game_info['genre_match'] = False

                for game_tag in game_object.tags.all():
                    if game_tag in game['matching_tags']:
                        match_score += TAG_MATCH_SCORE
                        game_info['matched_tags'].append(game_tag)
                    else:
                        game_info['unmatched_tags'].append(game_tag)

                game_info['match_score'] = match_score
                all_games_info.append(game_info)

            ctx = {
                'sorted_all_game_information': sorted(
                    all_games_info, key=itemgetter('match_score'), reverse=True
                ),
                'user_favorites': {
                    'favorite_tags_top_6': user_tags,
                    'favorite_genre': user_genre,
                    'favorite_developer': user_developer
                }
            }

            return render(
                request,
                template_name='recommendation/recommendation_preference_result.html',
                context=ctx
            )
            

        messages.add_message(request, messages.ERROR, _('Form invalid'))
        return HttpResponseRedirect(reverse('recommendation'))

    @staticmethod
    def _assign_matching_tags_to_game(user_tags, all_games_qs):
        
        """Returns all game objects with game tags which match user's favorites"""
        games_and_matching_tags = []
        
        for game in all_games_qs:
            print(game.tags.all)
            matching_tags = list(set(game.tags.all()).intersection(user_tags))
            games_and_matching_tags.append({
                'game_object': game,
                'matching_tags': matching_tags
            })
        return games_and_matching_tags
