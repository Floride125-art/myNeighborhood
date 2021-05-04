from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import *
from django.views import generic
@login_required(login_url='/accounts/login/')
def home(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'home.html',{"neighbourhoods":neighbourhoods,})
def add_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')
    else:
        form = NewProfileForm()
    return render(request, 'edit_profile.html', {"form":form})    