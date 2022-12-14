from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def HomePage(request):
    return render(request,'auth_system/index.html', {})

def Register(request):
    if request.method =="POST":
        #get information from the template
        fname = request.POST.get("fname")
        lname = request.POST.get("sname")
        name = request.POST.get("uname")
        email = request.POST.get("email")
        password = request.POST.get("pass")

        #create a user
        new_user = User.objects.create_user(name, email, password)#order username mail password then we add if there other items
        new_user.first_name =fname
        new_user.last_name= lname 
        new_user.save()#save user
        return redirect("login-page")#if he submit redirect to login page name taken from the url file
        
    return render(request,'auth_system/register.html',{})

def Login(request):
    if request.method =="POST":
        name = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(request,username=name, password=password)#fetch if the user exsist
        if user is not None:
            login(request, user)#login if user exsist
            return redirect("home-page")
        else:
            return HttpResponse("Error , user does not exist")
    return render(request,'auth_system/login.html',{})

def Logoutuser(request):
    logout(request)
    return redirect("login-page")
    
def Test(request):
    return render(request,'auth_system/test.html',{})