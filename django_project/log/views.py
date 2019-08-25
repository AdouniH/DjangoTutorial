
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .form import Log_form
from .models import Visitor

def main_page(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {})

    form = Log_form()

    if request.method == 'POST':
        code = request.POST['name']
        # TODO: OneToOne Management
        comp_object = Visitor.objects.filter(code=code)
        if comp_object:
            name = comp_object[0].name
            pwd = comp_object[0].pwd
            user = authenticate(username=name, password=pwd)
            if not user:
                user = User.objects.create_user(username=name, password=pwd)

            login(request, user)
            return redirect('/cv_houssem_adouni/')

            # return render(request, 'home.html', {})
        else:
            return render(request, 'homepage.html', {"form": form, 'msg': 'Veuillez entrer un bon code'})

    return render(request, 'homepage.html', {"form": form})


def disconnect(request):
    logout(request)
    form = Log_form()
    context = {"form": form}
    return render(request, 'homepage.html', context)

def mycv(request):
    return render(request, 'mycv.html', {})
