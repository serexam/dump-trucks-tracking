from django.shortcuts import render
from .models import DumpTruck
from .models import DumpTruckModel

def index(request):
	cars = DumpTruck.objects.all()
	return render(request, 'cars/cars_list.html', {'cars': cars})
