from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def help(request):
    dic1 = {
        "call_from" : "help - views - help"
    }
    return render(request,'help.html', context = dic1)