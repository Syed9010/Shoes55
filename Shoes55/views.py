from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Product

# Create your views here.
def Shoes55(request):
    return render(request,'Homepage.html')

def Cartpage(request):
    return render(request,'cart.html')

def Signinpage(request):
    return render(request,'signin.html')

def Register(request):
    return render(request,'register.html')

def Sports(request):
    return render(request,'sports.html')

def Menc(request):
    return render(request,'Mencasul.html')

def Menf(request):
    return render(request,'Menformal.html')

def Women(request):
    return render(request,'womens.html')

def nike(request):
    return render(request,'nike.html')

def redtape(request):
    return render(request,'Redtape.html')

def spark(request):
    return render(request,'Spark.html')

def addidas(request):
    return render(request,'addidas.html')

def Wsport(request):
    return render(request,'wsport.html')

def Userlogin(request):
    if request.method=='POST':
        vuemail=request.POST.get('uemail')
        vupasswd=request.POST.get('upasswd')
        user=auth.authenticate(uemail=vuemail,upasswd=vupasswd)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Successfully logged in!!")
            return redirect('/Shoes55')
        else:
            messages.success(request,"kindly login again!!!!")
            return redirect('/Shoes55')
'''
def registerUser(request):
 if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        uemail=request.POST.get('uemail')
        upasswd=request.POST.get('upasswd')
        cpasswd=request.POST.get('cpasswd')
        if upasswd==cpasswd:
            if Product.objects.filter(uname=vuname).exists():
                messages.success(request,"The username already registered here....")
                return redirect('/register')
            elif Product.objects.filter(uemail=vuemail).exists():
              messages.success(request,'The Email addresssis already available')
            return redirect('/register')  
        else:
                newuser=Product()
                newuser.fname=vfname
                newuser.lname=vlname
                newuser.uname=vuname
                newuser.uemail=vuemail
                newuser.upasswd=vupasswd
                newuser.save()
                return redirect('/Signin')
'''           
            
def registerUser(request):
    if request.method=="POST":
        # Get the post parameters
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        uemail=request.POST['uemail']
        upasswd=request.POST['upasswd']
        cpasswd=request.POST['cpasswd']

        # check for errorneous input
        
        if (upasswd!= cpasswd):
             messages.error(request, " Passwords do not match")
             return redirect('/Signin')
        
        # Create the user
        myuser = User.objects.create_user(uname, uemail, upasswd)
        myuser.fname= fname
        myuser.lname= lname
        myuser.save()
        messages.success(request, " Your registration has been successfully created")
        return redirect('/Signin')

    else:
        return HttpResponse("404 - Not found")
'''          
def registerUser(request):
    if request.method== 'POST':
        vfname=request.POST.get('fname')
        vlname=request.POST.get('lname')
        vuname=request.POST.get('uname')
        vemail=request.POST.get('email')
        vpasswd=request.POST.get('passwd')
        vcpasswd=request.POST.get('cpasswd')
        if vpasswd==vcpasswd:
            if User.objects.filter(uname=vuname).exists():
                messages.success(request, "The username is already registered here...")
                return redirect('/Reg')
            elif User.objects.filter(email=vemail).exists():
                messages.success(request, 'The Email address is already avilable')
                return render('/Reg')
            else:
                newuser=User.objects.create_user(fname=vfname,lname=vlname,uname=vuname,email=vemail,passwd=vpasswd)
                newuser.save()
                messages.success(request,'User Registration done')
                return redirect('/Signin')

def insertuser(request):
    if request.method=='POST':
        vfname=request.POST.get('fname')
        vlname=request.POST.get('lname')
        vuname=request.POST.get('uname')
        vuemail=request.POST.get('uemail')
        vupasswd=request.POST.get('upasswd')
        emp=registration()
        emp.fname=vfname
        emp.lname=vlname
        emp.uname=vuname
        emp.uemail=vuemail
        emp.upasswd=vupasswd
        emp.save()
        return redirect('/Signin')        
'''  

def logOut(request):
    auth.logout(request)
    messages.success(request,'Successfully logged out!!')
    return redirect('/Signin')