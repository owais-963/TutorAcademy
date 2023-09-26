from django.db import models
from datetime import datetime

# Create your models here.


class ContactUS(models.Model):
    tuID = models.CharField(max_length=200, primary_key=True, unique=True, null=False, blank=False)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    add = models.TextField()
    fee = models.CharField(max_length=20)
    add_n = models.TextField(null=True, blank=True)
    status = models.IntegerField()
    date = models.DateField(datetime.now().today(),null=True, blank=True)


class Tutor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    nic = models.CharField(primary_key=True, unique=True, max_length=50)
    add = models.TextField()
    pas = models.CharField(max_length=1000)
    pic = models.ImageField(upload_to="images/",default="images/profile.jpg")
    qua = models.CharField(max_length=250)
    inst = models.CharField(max_length=250)
    about = models.TextField(null=True, blank=True)
    approval = models.IntegerField()
    exp = models.TextField()
    sub = models.TextField()
    ach = models.TextField(null=True, blank=True)
    date = models.DateField(datetime.now().today(),null=True, blank=True)
    # math = models.BooleanField()
    # sci = models.BooleanField()
    # geo = models.BooleanField()
    # hist = models.BooleanField()
    # bus = models.BooleanField()
    # arts = models.BooleanField()


class TutorApplied(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    tution = models.ForeignKey(ContactUS, on_delete=models.CASCADE)
    approval = models.IntegerField()
