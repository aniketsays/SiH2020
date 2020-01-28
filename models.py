from django.db import models
from django.contrib.auth.models import User


class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=10, null=True)
    username = models.CharField(max_length=100, default="")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact = models.IntegerField(default=0)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)


class inputCrops(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    #region = models.CharField(max_length=10)
    subregion = models.CharField(max_length=100)
    soil = models.CharField(max_length=100)


class Financial(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=10)
    username = models.CharField(max_length=100, default="")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact = models.IntegerField(default=0)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    firmname = models.CharField(max_length=50)
    employee = models.CharField(max_length=25)


class NonFinancial(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=10)
    username = models.CharField(max_length=100, default="")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact = models.IntegerField(default=0)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    firmname = models.CharField(max_length=50)
    employee = models.CharField(max_length=25)


# class outputCrops(models.Model):
#     subregion = models.CharField(max_length=100)
#     crop = models.CharField(max_length=100)
#     soil = models.CharField(max_length=50)
#     pesticides = models.CharField(max_length=100)
#     fertilizers = models.CharField(max_length=50)
#     pests = models.CharField(max_length=100)
#     rainfall=models.CharField(max_length=100)



# class login(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     #birthdate = models.DateField()

    # firstname = request.POST.get('firstname')
    # username = request.POST.get('username')
    # lastname = request.POST.get('lastname')
    # password = request.POST.get('password')
    # contact = request.POST.get('contact')
    # city = request.POST.get('city')
    # state = request.POST.get('state')
    # country = request.POST.get('country')
    # gender = request.POST.get('gender')

