 

 
from django.shortcuts import redirect, render
from django.contrib import messages
from home.views import home
from django.contrib.auth.models import User,auth
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required


# Create your views here.
@never_cache
def home(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            return render(request, 'admin.html')
        else:
            return redirect('login')



@never_cache
def login(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            return redirect('home')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
          
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST.get('username')
        email=request.POST['email']
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'! Username Is Taken !')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'! Email is already used !')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User Created')
                return redirect('/')
        else:
            messages.info(request,'!! The password is not matching !!')
            return redirect('register')
        return redirect('/')
    else:
        return render (request,'register.html')    

@never_cache
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('/')
    








            

