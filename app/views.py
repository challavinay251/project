from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserDataForm
from .models import UserData

def input_data(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_data')
    else:
        form = UserDataForm()
    return render(request, 'app/input_data.html', {'form': form})

def display_data(request):
    users = UserData.objects.all()
    return render(request, 'app/display_data.html', {'users': users})

def home(request):
    users = UserData.objects.all()
    return render(request, 'app/home.html', {'users': users})
