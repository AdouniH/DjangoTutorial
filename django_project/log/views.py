
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .form import Login_form, Log_form
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Visitor

def main_page(request):
    form = Log_form()



    # login
    if request.method == 'POST':
        code = request.POST['name']
        # TODO: OneToOne Management
        comp_object = Visitor.objects.filter(code=code)
        if comp_object:
            name = comp_object[0].name
            pwd = comp_object[0].pwd

            return HttpResponse(comp_object[0].name)
        #
    return render(request, 'homepage.html', {"form": form})

    # return render(request, 'home.html', {})


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
