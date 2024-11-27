from django.db import models
from Musicians.models import Musician_Model
import datetime

# Create your models here.


class Album_Model(models.Model):
    Album_name = models.CharField(max_length= 50)
    musician = models.ForeignKey(Musician_Model, on_delete= models.CASCADE)
    release_date = models.DateField(null= True, blank= True, default= datetime.date.today)
    CHOICES = {
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    }
    
    Rating = models.IntegerField(choices= CHOICES)
    
    
    def __str__(self):
        return self.Album_name
    
    
    
    