from django.shortcuts import render, redirect
from . froms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='my-login')
def homepage(request):

    return render(request, 'home.html')



def register(request):
    form=CreateUserForm()
    if request.method =="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
        
        else:
            messages.error(request, 'Invalid Information')
            return redirect('register')
        
        


        
    context={'registerform':form}
    return render(request, 'register.html',context=context)

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or Password is incorrect')
                return redirect('my-login')
    
    context={'Loginform':form}
    return render(request, 'my-login.html',context=context)

def user_logout(request):
    auth.logout(request)
    return redirect('my-login')