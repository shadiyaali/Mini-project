from django.shortcuts import render

# Create your views here.
import email
from django.shortcuts import redirect, render
from django.contrib import messages
from home.views import home
from django.contrib.auth.models import User,auth
from django.views.decorators.cache import never_cache


@never_cache
def admin_log(request):
    if request.user.is_authenticated or request.user.is_superuser:
        return redirect(admins)
    return render(request,'admin_login.html')


@never_cache
def admins(request):
    if request.user.is_authenticated:
        if 'a' in request.POST:
            a = request.POST['a']
            details=User.objects.filter(first_name__icontains=a)
        else:
            details= User.objects.all()
        return render(request,'admin.html',{'details':details})
    return redirect(admin_log)

       
@never_cache
def admin_login(request):
    if request.user.is_authenticated or request.user.is_superuser:
        return redirect(admins)
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None and user.is_superuser:
            auth.login(request,user)
            return redirect(admins)
        else:
            messages.info(request, 'User Name Not Valid')
            return redirect(admin_log)
    else:
        return render(request,'admin_login.html')


@never_cache
def admin_logout(request):
    if request.user.is_authenticated or request.user.is_superuser:
        auth.logout(request)
    return redirect('/')



def admin_ins(request):
    return render(request,'admin_insert.html')

def admin_insert(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']   
        last_name=request.POST['last_name']     
        username=request.POST['username']    
        password=request.POST['password']    
        password2=request.POST['password2']    
        email=request.POST['email'] 


        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'   !! Username Is Taken !! ') 
                return redirect('admin_ins')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'  !! Email is already used !! ')
                return redirect('admin_ins')
            else:
                user= User.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name)
                user.save()
                return redirect(admins)
        else:
            messages.info(request,'!! The password are not matching !!')
            return redirect('admin_ins')


def admin_edit(request,id):
    
    user = User.objects.get(id=id)
    return render(request,'admin_edit.html',{'user_details': user})


def admin_update(request,id):
    if request.method == 'POST':
         
        user= User.objects.get(id=id)
        first_name=request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')


        user.first_name =  first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()
        return redirect(admins)


def admin_delete(request,id):
    user_del=User.objects.get(id=id)
    user_del.delete()
    user = User.objects.all()
    return redirect(admins)


