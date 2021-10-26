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

def list(request):
    redis_url = os.getenv('REDISTOGO_URL')
    parse.uses_netloc.append('redis')
    url = parse.urlparse(redis_url)
    r = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)

    list_name = [str(key)[14:-1] for key in r.keys("*")]
    context = {'date': list_name}
    print(list_name)
    
    return render(request, 'channels-list.html',context)