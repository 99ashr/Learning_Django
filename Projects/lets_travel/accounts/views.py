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
                print('Username is taken')
            elif User.objects.filter(email=email).exists():
                print("Email id already exists")
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created!')
        else:
            print("Password is not matching... ")
        return redirect('/')
    else:
        return render(request, 'register.html')
