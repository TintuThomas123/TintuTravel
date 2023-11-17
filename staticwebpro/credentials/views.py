from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        username1=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email1=request.POST['emailid']
        password1=request.POST['password']
        cpassword1=request.POST['cpassword']
        if password1==cpassword1:
            if User.objects.filter(username=username1).exists():
                messages.info(request,"Username already taken...")
                return redirect("register")
            elif User.objects.filter(email=email1).exists():
                messages.info(request," already existing e-mail id")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username1,first_name=fname,last_name=lname,email=email1,password=password1)
                user.save();
                print("user created..")
                return redirect('login')
        else:
            messages.info(request,"password not matching....")
            return redirect("register")
        return redirect("/")
    return render(request, "register.html")

def login(request):
    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']
        user=auth.authenticate(username=username1,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
