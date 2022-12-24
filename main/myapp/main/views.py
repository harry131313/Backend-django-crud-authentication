from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from itertools import chain 
from .models import Profile, patientregistration
from .forms import PatientCreate

# Create your views here.
# def login(req):
#     return render(req, 'login.html')

def register(req):
    
    if req.method == "POST":
        username = req.POST['username']
        labname = req.POST['labname']
        location = req.POST['location']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']
        
        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(req, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(req, 'Username taken')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                #create profile oject for new user
                user_model = User.objects.get(username = username )
                new_profile = Profile.objects.create(user = user_model, labname = labname, location = location )
                new_profile.save()
                return redirect('login')
        else:
            messages.info(req, 'Password not matched')
            return redirect('register')
    else:         
        return render(req, 'register.html')

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        
        user = auth.authenticate(username = username , password = password)
        
        if user is not None:
            auth.login(req, user)
            return redirect('dashboard')
        else:
            messages.info(req, 'Fake Credentail')
            return redirect('register')
    else:
        return render(req, 'login.html')
    
@login_required(login_url='login')   
def home(req):
    return render(req, 'home.html')
    
    
def signout(req):
    auth.logout(req)
    return redirect('login')

@login_required(login_url='login')  
def patientregistration1(req):
    if req.method == "POST":
        user = req.user.username
        firstname = req.POST['firstname']
        lastname = req.POST['lastname']
        gender = req.POST['gender']
        address = req.POST['address']
        
       
        age = req.POST['age']
        email = req.POST['email']
        mobile = req.POST['mobile']
        dateofbirth = req.POST['dateofbirth']
        passport = req.POST['passport']
        pannumber = req.POST['pannumber']
        
        
        user_model = User.objects.get(username= user)
        new_patient= patientregistration.objects.create(user = user_model, firstname=firstname, lastname=lastname, gender=gender, address=address,
                                                        age=age, email=email, mobile=mobile, dateofbirth=dateofbirth, passport=passport,
                                                        pannumber=pannumber)
        new_patient.save()
        return redirect('/dashboard/')
        
    return render(req, 'patientregistration.html')

@login_required(login_url='login')  
def billing(req):
    return render(req, 'billing.html')

@login_required(login_url='login')  
def dashboard(req):
    user_object = User.objects.get(username = req.user.username)
    # user_profile = patientregistration.objects.get(user = user_object)
    user_profile = patientregistration.objects.filter(user= user_object)
    return render(req, 'dashboard.html', {'user_profile': user_profile})

@login_required(login_url='login')  
def delete(req, pk):
    given_id = int(pk)
    del_patient = patientregistration.objects.get(id=given_id)
    del_patient.delete()
    return redirect('dashboard')
    
@login_required(login_url='login')  
def edit(req, pk):
    given_id = int(pk)
    patient_edit = patientregistration.objects.get(id = given_id)
    edit_form = PatientCreate(req.POST or None, instance=patient_edit )
    if edit_form.is_valid():
        edit_form.save()
        return redirect('dashboard')
    return render(req, 'edit.html', {'edit_form': edit_form})
    