import re
from django.shortcuts import render
import redis
from urllib import parse 
import os
def room(request, room_name):

    redis_url = os.getenv('REDIS_URL')
    parse.uses_netloc.append('redis')
    url = parse.urlparse(redis_url)
    redis_get = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)

    # redis_get = redis.Redis()
    message_info = redis_get.lrange(room_name, 0,-1)
    maga = [str(arr)[2:-1] for arr in message_info]
    print(message_info)
    print(maga)
    return render(request, 'room.html', {
        'room_name': room_name,
        "past_message" : maga
    },)

def hub(request):
    return render(request, 'index.html')

def list(request):
    redis_url = os.getenv('REDIS_URL')
    parse.uses_netloc.append('redis')
    url = parse.urlparse(redis_url)
    r = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)

    # r = redis.Redis()
    list_name = [str(key)[14:-1] for key in r.keys("*")]
    context = {'date': list_name}
    print(list_name)
    
    return render(request, 'channels-list.html',context)