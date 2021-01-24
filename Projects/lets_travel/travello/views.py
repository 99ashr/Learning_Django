from django.shortcuts import render

# Create your views here.

from .models import Destination


def index(request):
    # print("index")
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps.'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Chennai'
    dest2.desc = 'Madrasi.'
    dest2.img = 'destination_2.jpg'
    dest2.price = 600
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Jaipur'
    dest3.desc = 'The pink city.'
    dest3.img = 'destination_3.jpg'
    dest3.price = 800
    dest3.offer = False

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})
