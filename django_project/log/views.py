
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .form import Login_form

def main_page(request):
    form = Login_form()

    # login
    if request.POST:
        user = authenticate(username=request.POST["user_name"], password=request.POST["user_pwd"])
        if user:
            login(request, user)

    # get IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # return variables to template
    context = {"form": form,
               "user": request.user.username,
               "auth": request.user.is_authenticated,
               "ip": ip
               }

    return render(request, 'homepage.html', context)

def disconnect(request):
    logout(request)
    form = Login_form()
    context = {"form": form,
                 "user": request.user.username,
                 "auth": request.user.is_authenticated
                 }
    return render(request, 'homepage.html', context)
