# web서버의 http헤더에 저장된 server_name을 받음. 
# haproxy가 잘 작동하나 테스트 용 

from django.shortcuts import render
from django.conf import settings

def home(request):
    server_name = request.META.get('HTTP_X_UPSTREAM_SERVER', 'UNKOWN')
    return render(request, 'home.html', {
        'server_name' : server_name
    })
