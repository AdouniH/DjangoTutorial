from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    return HttpResponse("this is blog view")


def detail(request):
    return HttpResponse("Here is detail view")
