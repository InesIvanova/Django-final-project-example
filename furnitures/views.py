from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Furniture

from accounts.models import ProfileUser


def has_access_to_modify(current_user, furniture):
    if current_user.is_superuser:
        return True
    elif current_user.id == furniture.user.id:
        return True
    return False


class FurnitureList(generic.ListView):
    model = Furniture
    template_name = 'furniture_list.html'
    context_object_name = 'furniture'


class UserFurnitureList(LoginRequiredMixin, generic.ListView):
    model = Furniture
    template_name = 'furniture_list.html'
    context_object_name = 'furniture'

    def get_queryset(self):
        user_id = int(self.request.user.id)

        try:
            user = ProfileUser.objects.all().filter(user__pk=user_id)[0]
            furniture = Furniture.objects.all().filter(user = user.pk)
            return furniture
        except:
            return []


class FurnitureDetail(LoginRequiredMixin, generic.DetailView):
    model = Furniture
    login_url = '/accounts/login/'
    context_object_name = 'furniture'
    template_name = 'furniture_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FurnitureDetail, self).get_context_data(**kwargs)
        owner = context['object'].user
        current_user = self.request.user
        if has_access_to_modify(current_user, owner):
            context['is_user_furniture'] = True
            return context
        context['is_user_furniture'] = False
        return context


class FurnitureDelete(LoginRequiredMixin, generic.DeleteView):
    model = Furniture
    login_url = 'accounts/login/'
    context_object_name = 'funrniture'

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        return render(request, 'furniture_delete.html', {'furniture': self.get_object()})

    def post(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        furniture = self.get_object()
        furniture.delete()
        return HttpResponseRedirect('/furniture/')




