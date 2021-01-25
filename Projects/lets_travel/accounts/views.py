from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken')
                return(redirect('register'))
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email id already exists")
                return(redirect('register'))
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'user created!')
                return redirect('login')
        else:
            messages.info(request, "Password is not matching... ")
            return(redirect('register'))
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')

    else:
        return render(request, 'login.html')


# TODO:
    #! redirect to login page if a user is not logged in to fetch the details of destination.


def logout(request):
    auth.logout(request)
    return redirect('/')
