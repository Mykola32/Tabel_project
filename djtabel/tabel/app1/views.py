from django.http import HttpResponseRedirect
from django.shortcuts import render

from app1.forms import FormBuyer
from app1.models import LogisticInfo


# Create your views here.

def index(request):
    return render(request, 'index.html')

def logforma(request):
    if request.method == 'POST':
        forma = FormBuyer(request.POST)
        if forma.is_valid():
            new_log_info = LogisticInfo(
                distance=request.POST['distance'],
                type_delivery=request.POST['type_delivery'],
                masa=request.POST['masa'],
                pib=request.POST['pib'],
                phone=request.POST['phone'],
                email=request.POST['email'],
            )
            new_log_info.save()
            return HttpResponseRedirect('/')
    else:
        forma = FormBuyer()
    return render(request, 'forma_buy.html', {'form': forma})