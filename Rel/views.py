from django import contrib
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, request
from django.views.generic import View


class HomeView(View):
    def get(self,request):

        # data = PPerson.objects.get(id=4)
        # data = PPerson.objects.all()


        # individual = PPerson.objects.get(id=1)
        # data = individual.address.street

        # obj1 = Address.objects.get(id=1)
        # data = obj1.pperson.name

        # obj1 = CCity.objects.get(id=1)
        # data = obj1.address_set.all()
        # data = obj1.address.street  --Error-- 'CCity' object has no attribute 'address'
        
        # obj1 = IInterest.objects.get(id=1)
        # data = obj1.pperson.name



# ONE TO ONE IS QUITE EASY..ITS STARITFORWARD BOTH THE WAYS
        # data = Address.objects.get(id=1).person
        # data = PPerson.objects.get(id=1).address.city


# ONE TO MANY / MANY TO ONE ie FOREIGNKEY 
        # data = Address.objects.get(id=2).city 
        # ------>> As class Address has city as one of the attribute,address to city is straitfw
        # ------>> but as city(attribute of Address) has FK relation,city to address is reverse relation so need to use _set.all()
        data = CCity.objects.get(id=1).address_set.all()


# MANY TO MANY  - Similar to Foreignkey relation

        # data = PPerson.objects.get(id=1).interests.all()
        # data = IInterest.objects.get(id=1).pperson_set.all()


        # data = PPerson.objects.get(id=1).address
        return render(request,'Rel/home.html',{'data':data})
