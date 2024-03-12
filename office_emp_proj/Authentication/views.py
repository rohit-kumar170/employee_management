from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_views(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #form.cleaned_data.get('username')
            return redirect('authentication:login')
    else:
        form=UserCreationForm()
    return render(request,'users/register.html',context={'form':form})
@login_required
def profilepage(request):
    return render(request,'users/profile.html')

        

