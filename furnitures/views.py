from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Furniture
from .forms import CreateFurnitureForm

from accounts.models import ProfileUser
from reviews.models import Review
from reviews.forms import ReviewForm


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
        context['reviews'] = Review.objects.all().filter(furniture=self.get_object())
        context['form'] = ReviewForm()
        # context['form'].fields['author'].initial = self.request.user.id
        print(context)
        owner = context['object'].user
        current_user = self.request.user
        if has_access_to_modify(current_user, owner):
            context['is_user_furniture'] = True
            return context
        context['is_user_furniture'] = False
        return context

    def post(self,request, pk):
        url = f'/furniture/details/{self.get_object().id}/'
        post_values = request.POST.copy()
        form = ReviewForm(post_values)

        if form.is_valid():
            author = ProfileUser.objects.all().filter(user__pk=request.user.id)[0]
            post_values['furniture'] = self.get_object()
            review = Review(
                content = post_values['content'],
                score = post_values['score'],
                furniture=self.get_object(),
                author=author
            )
            review.save()
            return HttpResponseRedirect(url)
        else:
            raise Exception(form.errors)


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


class FurnitureCreate(LoginRequiredMixin, generic.CreateView):
    model = Furniture
    template_name = 'furniture_create.html'
    form_class = CreateFurnitureForm
    success_url = '/furniture/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)










