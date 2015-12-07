from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def home_page(request):
    return render(request, 'grad_forms/home.html')

def ms_pos_form(request):
    if request.method == 'POST':
        form = forms.MSPoSCoursework(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
    else:
        form = forms.MSPoSCoursework()
    return render(request, 'grad_forms/form_template.html', {'form': form})

def phd_pos_form(request):
    return render(request, 'grad_forms/form_template.html')

def meng_pos_form(request):
    return render(request, 'grad_forms/form_template.html')

def independent_study_form(request):
    return render(request, 'grad_forms/form_template.html')
