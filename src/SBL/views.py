from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    user = request.user
    hello = 'hello'
    context ={
        'user': user,
        'hello': hello
    }
    return render(request, 'main/index.html',context)
    # return HttpResponse(' home is working')