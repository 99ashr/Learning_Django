from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'AShr'})


def add_get(request):
    print("GET Method----")
    v1 = int(request.GET['num1'])
    v2 = int(request.GET['num2'])
    res = v1+v2
    return render(request, 'result.html', {'result': res})


def add_post(request):
    print("POST Method----")
    v1 = int(request.POST['num1'])
    v2 = int(request.POST['num2'])
    res = v1+v2
    return render(request, 'result.html', {'result': res})
