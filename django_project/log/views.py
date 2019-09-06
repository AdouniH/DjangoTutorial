
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .form import Log_form, TokenrdvForm
from .models import Visitor, RendezVous
from .business_module.business import arrange

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

@login_required
def mycv(request, section):
    context = {}
    if section in ["experience", "projets", "competences", "diplomes"]:
        context[section] = section

    return render(request, 'mycv.html', context)

@login_required
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
    phone_crenaux = []
    if section in ["phone", "sur_place"]:
        context[section] = section

    if section == "phone":
        phone_crenaux = RendezVous.objects.filter(rdv_type="phone")

    elif section == "sur_place":
        phone_crenaux = RendezVous.objects.filter(rdv_type="sur_place")

    l = []
    for i in phone_crenaux:
        x = {}
        x["day"] = i.time.strftime('%d/%m/%Y')
        x["day_name"] = day_mapping[i.time.strftime('%A')]
        x["hour"] = i.time.strftime('%H:%M')
        x["id"] = i.id
        x["comparator"] = i.time.strftime('%Y%m%d')
        l.append(x)
    sorted_creneau = arrange(l)

    context["rdvs"] = sorted_creneau


    return render(request, 'rdv.html', context)

@login_required
def rdv_fix(request, creneau_id):
    if request.method == "POST":
        form = TokenrdvForm(request.POST)
        if form.is_valid():
            form.cleaned_data["name"] = "haha"
            rdv_object = form.save(commit=False)
            rdv_object.rdv_shift = RendezVous.objects.get(id=creneau_id)
            rdv_object.save()
            return HttpResponse("SUCCESS")
        else:
            return HttpResponse("form is not valid")
    form = TokenrdvForm()
    rdv_creneau = RendezVous.objects.get(id=creneau_id)
    creneau_type = rdv_creneau.rdv_type
    context = {}
    context[creneau_type] = creneau_type
    context["form"] = form
    context["rdv_id"] = creneau_id
    return render(request, 'rdv_form.html', context)

@login_required
def form_submit(request, creneau_id):
    context = {}
    context["rdv_id"] = creneau_id

    return render(request, 'form_submit.html', context)
