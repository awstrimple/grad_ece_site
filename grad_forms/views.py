from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'grad_forms/home.html')

def ms_pos_form(request):
    return render(request, 'grad_forms/form_template.html')

