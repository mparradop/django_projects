from django.shortcuts import render
from main import models as core


# Create your views here.

def main(request):
    return render(request,'main.html')

def hello(request):
    cia = core.Company.objects.get(id=2)

    context = {
        "name":cia.__str__
        }
    return render(request, "hello.html", context)