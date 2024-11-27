from django.shortcuts import render
from Albums.models import Album_Model

def home(req):
    data = Album_Model.objects.all()
    return render(req, 'home.html', {'data' : data})


