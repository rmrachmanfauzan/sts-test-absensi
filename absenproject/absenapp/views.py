from django.contrib.auth import login as auth_login,logout as auth_logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from .forms import RegistrationForm
from .models import User,Absen

def register(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(email=email, password=password)
            auth_login(request, user)
            return redirect('/app')
        else:
            context['form'] = form
    else:  
        form = RegistrationForm()
        context['form'] = form
    return render(request, 'register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/app')
        else:
            print('user not found')
            return redirect('/app/login')
    else:    
        return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('absenapp:login')

def index(request):
    if request.method == 'GET':
        context = {}
        try:
            start_date = request.GET["date_start"]
            end_date =request.GET["date_end"]
            absen = Absen.objects.filter(tanggal__lte=end_date, tanggal__gt=start_date).order_by('-id')
        except:
            absen = Absen.objects.filter().order_by('-id')
        
        context['datas'] = absen
        return render(request, 'home.html', context)

def checkin(request):
    if request.method == 'GET':
        absen = Absen(  
                        user= request.user, 
                        tanggal=datetime.today(),
                        absen_in = datetime.today()
                    )
        absen.save()
        return redirect('/app')

def checkout(request,absen_id):
    if request.method == 'GET':
        absen = Absen.objects.get(id=absen_id)
        absen.absen_out = datetime.today()
        absen.save()
        
        return redirect('/app')