from django.shortcuts import render, redirect
from . import forms, models

# Create your views here.


def add_musician(req):
    if req.method == "POST":
        musician_form = forms.Musician_Form(req.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("add_musician")
        
    else:
        musician_form = forms.Musician_Form()
    
    return render(req, 'add_musician.html', {'form' : musician_form})



def edit_musician(req, id):
    musician = models.Musician_Model.objects.get(pk = id)
    musician_form = forms.Musician_Form(instance = musician)
    
    if req.method == "POST":
        musician_form = forms.Musician_Form(req.POST, instance = musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("home")
        
    return render(req, 'add_musician.html', {'form' : musician_form})

