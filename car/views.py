from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_cars(request):
    cars = Car.objects.all()
    return render(request,'car/list.html',{'cars':cars})

@login_required
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            Car.objects.create(
                brand=form.cleaned_data['brand'],
                model = form.cleaned_data['model'],
                year = form.cleaned_data['year'],
                color = form.cleaned_data['color'],
                price = form.cleaned_data['price'],
                mileage = form.cleaned_data['mileage']
            )
            return redirect('list')
    else:
        form = CarForm()
    return render(request,'accounts/create_car.html',{'form':form})

def read_car(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request,'car/read_car.html',{'car':car})

@login_required
def update_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = CarForm(request,POST)
    return render(request,'accounts/update_car.html',{'car':car})