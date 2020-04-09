from django.shortcuts import render
from django.http import HttpResponse
from First_app.models import Topic,Webpage,AccessRecord

# Create your views here.

def index(request):
    records = AccessRecord.objects.order_by('date')
    date_dict = {'access_record' : records}
    return render(request,'first_app/index.html',context= date_dict)
