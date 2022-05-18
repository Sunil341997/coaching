
from django.db import models


class Coaches(models.Model):
    type = ((1, 'ICF ACC'),
            (2, 'ICF PCC'),
            (3, 'ICF MCC'),)

    id                         = models.AutoField(max_length=10, primary_key=True,null=False,blank=False)
    name                       = models.CharField(max_length=25,null=False,blank=False,default=True)
    email                      = models.EmailField(max_length = 50,null=False,blank=False,unique=True)
    pic                        = models.FileField(upload_to="media/",null=True,blank=True)
    password                   = models.CharField(max_length=1024,null=True,blank=True)
    linked_in                  = models.CharField(max_length=100,null=True,blank=True)
    charge                     = models.CharField(max_length=100,null=True,blank=True)
    certi                      = models.CharField(choices=type, max_length=2,null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","password"]
    
    def __str__(self):
        return self.email 


class Coachees(models.Model):
    id                         = models.AutoField(max_length=10,primary_key=True,null=False,blank=False)
    name                       = models.CharField(max_length=25,null=False,blank=False,default=True)
    email                      = models.EmailField(max_length = 50,null=False,blank=False,unique=True)
    pic                        = models.FileField(upload_to="media/",null=True,blank=True)
    phone                      = models.CharField(max_length=10,null=True,blank=True)
    password                   = models.CharField(max_length=1024,null=True,blank=True)