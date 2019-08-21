
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .form import Login_form
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def main_page(request):

    if not request.user.is_authenticated:

        form = Login_form()

        # login
        if request.method == 'POST':
            usor = authenticate(username=request.POST["user_name"], password=request.POST["user_pwd"])
            if usor:
                login(request, usor)
                return render(request, 'home.html', {})

        return render(request, 'homepage.html', {"form": form})

    return render(request, 'home.html', {})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            usor = authenticate(username=request.POST["user_name"], password=request.POST["user_pwd"])
            login(request, usor)
            return render(request, 'home.html', {'form': form})
        else:
            return HttpResponse("NO")
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

def disconnect(request):
    logout(request)
    form = Login_form()
    context = {"form": form,
                 "user": request.user.username,
                 "auth": request.user.is_authenticated
                 }
    return render(request, 'homepage.html', context)
