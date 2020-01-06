from django.forms import (CheckboxSelectMultiple, Form, ModelChoiceField, ModelMultipleChoiceField, Select)
from django.utils.translation import ugettext_lazy as _

from developer.models import Developer
from genre.models import Genre
from tag.models import Tag
from django import forms

all_tags = Tag.objects.all()
all_developers = Developer.objects.all()
all_genres = Genre.objects.all()


class ChooseTagsForm(forms.Form):
    genre = ModelChoiceField(
        queryset=all_genres.order_by('name'),
        widget=Select
    )
    developer = ModelChoiceField(
        queryset=all_developers.order_by('name'),
        widget=Select
    )
    tags = ModelMultipleChoiceField(
        label=_('Tags (Select no more than 5)'),
        queryset=all_tags.order_by('name'),
        widget=CheckboxSelectMultiple(attrs={'class': 'checkboxmultiple'}))

    def clean_tags(self):
        if len(self.cleaned_data['tags']) > 5:
            raise forms.ValidationError('Select no more than 3.')
        return self.cleaned_data['tags']
    