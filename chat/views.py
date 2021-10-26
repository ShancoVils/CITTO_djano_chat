from django.shortcuts import render
import redis
 
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })

def hub(request):
    return render(request, 'index.html')

def list(request):
    r = redis.Redis()
    list_name = [str(key)[14:-1] for key in r.keys("*")]
    context = {'date': list_name}
    print(list_name)
    
    return render(request, 'channels-list.html',context)