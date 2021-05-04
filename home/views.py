from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import logout,authenticate,login
from home.models import Contact
# password for user harry is harry&&&***
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def loginuser(request):
    if request.method=="POST":
        #check if user have enter correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
    # A backend authenticated the credentials
            login(request,user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
             return render(request,'login.html')
    return render(request,'login.html')
    
def logoutuser(request):
    logout(request)
    return redirect('/login')
       
    
def createusers(request):
    if request.method=="POST":
        Username=request.POST.get("username")
        Password=request.POST.get("password")
        user = User.objects.create_user(Username, "dufalt@gmail.com",Password)
        user.save()
        messages.success(request, 'Your Account is Successfully Created!')
    return render(request,'createuser.html')
def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page hunny")
def service(request):
    return render(request,'service.html')
    # return HttpResponse("This is service page hunny")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contactt = Contact(name = name,email=email,phone=phone,desc=desc,date=datetime.today())
        contactt.save()
        messages.success(request, 'Your Details is Successfully Saved!')
    return render(request,'contact.html')