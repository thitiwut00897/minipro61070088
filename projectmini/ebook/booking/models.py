from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=50)
    open_time = models.TimeField((""), auto_now=False, auto_now_add=False)
    close_time = models.TimeField((""), auto_now=False, auto_now_add=False)
    capacity = models.IntegerField()

class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)

class Booking(models.Model):
    roomid = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField("", auto_now=False, auto_now_add=False)
    end_time = models.TimeField("", auto_now=False, auto_now_add=False)
    description = models.TextField()
    status = models.BooleanField(default=False)
    status_remark = models.TextField('')
    bookby = models.ForeignKey(Users, on_delete=models.CASCADE)
    bookdate = models.DateField(auto_now=True, auto_now_add=False)

