from django.db import models

# Create your models here.
class Advisor(models.Model):
    Advisor_Name =models.CharField(max_length=250)
    Advisor_Photo_URL = models.ImageField(upload_to='images/')


class User(models.Model):
    Name =models.CharField(max_length=250)
    Email = models.EmailField()
    Password = models.CharField(max_length=25)

class Userlogin(models.Model):
    Email = models.EmailField()
    Password = models.CharField(max_length=25)


class Advisorbook(models.Model):
    Booking_time  =models.DateTimeField()
