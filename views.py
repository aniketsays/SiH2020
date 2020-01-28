from django.shortcuts import render, redirect, reverse
from .models import Farmer, inputCrops, Financial, NonFinancial
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from django.db import IntegrityError
# from .modelfilename import predict
from django.contrib import auth


# lis = predict(input1, in2, in3)

def signupfarmer(request):
    if request.method == 'POST':
        try:
            firstname = request.POST.get('firstname')
            username = request.POST.get('username')
            lastname = request.POST.get('lastname')
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
            contact = request.POST.get('contact')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            gender = request.POST.get('gender')

            if firstname == "" or password == "" or repassword == "":
                return render(request, 'crops/login.html')

            user = User.objects.create_user(username=username, password=password)

            farmer = Farmer(firstname=firstname, username=username, lastname=lastname, password=password,
                            contact=contact, city=city, state=state, country=country, user=user)
            farmer.save()

            auth.login(request, user)
            return redirect(reverse("inputcrops"))

        except IntegrityError:
            return render(request, 'crops/farmerReg.html')

        # except HttpResponseForbidden:
        #     return render(request, 'crops/farmerReg.html')

    elif request.method == 'GET':
        return render(request, "crops/farmerReg.html")

    return redirect(reverse("inputcrops"))


# def logicml(farmer):


def inputcrops(request):
    if request.method == 'POST':
        try:

            farmer = Farmer.objects.get(user=request.user)
            subregion = request.POST.get('Sub-Region')
            print(subregion)
            # region = request.POST.get('region')
            soil = request.POST.get('soil')

            # logicml(farmer)

            # request.data['subregion']
            # print(subregion)
            inputCrops = inputCrops(subregion=subregion, soil=soil, farmer=farmer)
            inputCrops.save()

            # login(request, farmer)

            return render(request, 'crops/op2.html')

        except HttpResponseForbidden:
            return render(request, 'crops/ip2.html')

    elif request.method == 'GET':
        return render(request, "crops/ip2.html")


def home(request):
    return render(request, 'crops/homepage.html')


def outputcrops(request):
    return render(request, 'crops/op2.html')


def signupfinancial(request):
    if request.method == 'POST':
        try:
            firstname = request.POST.get('firstname')
            username = request.POST.get('username')
            lastname = request.POST.get('lastname')
            password = request.POST.get('password')
            contact = request.POST.get('contact')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            gender = request.POST.get('gender')
            firstname = request.POST.get('firmname')
            employee = request.POST.get('employee')

            if firstname == "" or password == "" or repassword == "":
                return render(request, 'crops/login.html')

            user = User.objects.create_user(username=username, password=password)
            financial = Financial(firstname=firstname, username=username, lastname=lastname, password=password,
                                  contact=contact, city=city, state=state, country=country, gender=gender,
                                  firmname=firmname,
                                  employee=employee)
            financial.save()

            login(request, user)
            return redirect(reverse("home"))

        except IntegrityError:
            return render(request, 'crops/FinancialReg.html')

        except HttpResponseForbidden:
            return render(request, 'crops/FinancialReg.html')

    elif request.method == 'GET':
        return render(request, "crops/FinancialReg.html")

    return redirect(reverse("home"))


def signupnonfinancial(request):
    if request.method == 'POST':
        try:
            firstname = request.POST.get('firstname')
            username = request.POST.get('username')
            lastname = request.POST.get('lastname')
            password = request.POST.get('password')
            contact = request.POST.get('contact')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            gender = request.POST.get('gender')
            firmname = request.POST.get('firmname')
            employee = request.POST.get('employee')

            if firstname == "" or password == "":
                return render(request, 'crops/login.html')

            user = User.objects.create_user(username=username, password=password)
            nonFinancial = NonFinancial(firstname=firstname, username=username, lastname=lastname, password=password,
                                        contact=contact, city=city, state=state, country=country, gender=gender,
                                        firmname=firmname,
                                        employee=employee)
            nonFinancial.save()

            login(request, user)
            return redirect(reverse("home"))

        except IntegrityError:
            return render(request, 'crops/NonFinancial.html')

        except HttpResponseForbidden:
            return render(request, 'crops/NonFinancial.html')

    elif request.method == 'GET':
        return render(request, "crops/NonFinancial.html")

    return redirect(reverse("home"))


def login(request):
    if request.method == 'POST':
        try:

            username = request.POST.get('username')

            password = request.POST.get('password')

            if firstname == "" or password == "":
                return render(request, 'crops/login.html')

            user = User.objects.create_user(username=username, password=password)
            farmer = Farmer(password=password, username=username)
            farmer.save()

            login(request, user)
            return redirect(reverse("inputcrops"))

        except IntegrityError:
            return render(request, 'crops/login.html')

        except HttpResponseForbidden:
            return render(request, 'crops/login.html')

    elif request.method == 'GET':
        return render(request, "crops/login.html")

        return redirect(reverse("inputcrops"))


def banks(request):
    return render(request, 'crops/Bank.html')

def suggestions(request):
    return render(request, 'crops/suggestions.html')

def weather(request):
    return render(request, 'crops/weather.html')

def gov(request):
    return render(request, 'crops/Gov.html')

