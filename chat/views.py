import re
from django.shortcuts import render
import redis
from urllib import parse 
import os
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })

def hub(request):
    return render(request, 'index.html')

