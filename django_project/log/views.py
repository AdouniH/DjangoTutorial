
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.http import HttpResponse
from .form import Log_form
from .models import Visitor, RendezVous

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
            return redirect('/cv_houssem_adouni/experience')

            # return render(request, 'home.html', {})
        else:
            return render(request, 'homepage.html', {"form": form, 'msg': 'Veuillez entrer un bon code'})

    return render(request, 'homepage.html', {"form": form})


def disconnect(request):
    logout(request)
    form = Log_form()
    context = {"form": form}
    return render(request, 'homepage.html', context)

def mycv(request, section):
    context = {}
    if section in ["experience", "projets", "competences", "diplomes"]:
        context[section] = section

    return render(request, 'mycv.html', context)


def rdv(request, section):
    day_mapping = {
        "Monday": "Lundi",
        "Tuesday": "Mardi",
        "Wednesday": "Mercredi",
        "Thursday": "Jeudi",
        "Friday": "Vendredi",
        "Saturday": "Samedi",
        "Sunday": "Dimanche"
    }
    context = {}
    if section in ["phone", "sur_place"]:
        context[section] = section

    if section == "phone":
        phone_crenaux = RendezVous.objects.all()
        l = []
        for i in phone_crenaux:
            l.append(i.time.strftime('%Y%m%d#%H:%M#%A'))

        # d = (l[0]).split('#')[0]
        d = {}
        for i in l:
            day = i.split('#')[0] + '-'+i.split('#')[2]
            d[day] = []

        for j in l:
            day = j.split('#')[0] + '-' + j.split('#')[2]
            hour = j.split('#')[1]

            d[day].append(hour)
        result = {}
        for key in d:
            new_key = "{} le {}/{}/{}:".format(day_mapping[key[9:]], key[6:8], key[4:6], key[:4])
            result[new_key] = d[key]

        context["rdv"] = result


    return render(request, 'rdv.html', context)