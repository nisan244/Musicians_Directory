from django.shortcuts import render, redirect
from . import forms, models

# Create your views here.

def add_album(req):
    if req.method == "POST":
        album_form = forms.Album_Form(req.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = forms.Album_Form()
    
    return render(req, 'add_album.html', {'form' : album_form})



def edit_album(req, id):
    album = models.Album_Model.objects.get(pk = id)
    album_form = forms.Album_Form(instance = album)
    
    if req.method == "POST":
        album_form = forms.Album_Form(req.POST, instance = album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    
    return render(req, 'add_album.html', {'form' : album_form})


def delete_album(req, id):
    album = models.Album_Model.objects.get(pk = id).delete()
    return redirect("home")


