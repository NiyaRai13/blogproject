from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login  as LOGIN


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        auth_user=User.objects.get(email=email)
        if auth_user:
            user = authenticate(request,username=auth_user.username,password=password)
            if user is not None:
                LOGIN(request,user)
                return redirect('index')
    return render(request, 'auth/login.html')

def logout_page(request):
    logout(request)
    return redirect('login')



def register(request):
    errors = {}
    if request.method=='POST':
        username= request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        
        if password != confirm_password:
            errors['confirm_password'] = "Password doesn't match."

        if not username:
            errors['username'] = "Username must be given."

        if not errors:
           user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
        #    user.set_password(password)
           user.save()
           return redirect('login')
        else:
            errors['error'] = "Failed to Register"
            return render(request, 'auth/login.html', {'errors':errors})
    return render(request,'auth/register.html')