from decouple import config
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic.list import ListView
from steam.models import Steam


from .models import Developer


class DeveloperListView(ListView):
    model = Developer
    template_name = 'developer/developer_list.html'



class DeveloperDeleteView(PermissionRequiredMixin, View):
    permission_required = 'developer.delete_developer'
    raise_exception = True

    def get(self, request, developer_id):
        developer = Developer.objects.get(id=developer_id)
        developer.delete()
        messages.add_message(request, messages.WARNING, _('Developer: {} has been deleted').format(developer.name))
        return HttpResponseRedirect(reverse('developer-list'))

