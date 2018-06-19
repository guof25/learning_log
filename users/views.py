from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, logout,authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("learning_logs:index"))

def register(request):
    if request.method !='POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user=authenticate(username=new_user.username,
            password = request.POST['password'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_Logs:index'))
    
    context = {'form':form}
    return render(request,'users/register.html',context)

