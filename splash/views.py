from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def home(request):
    pic = Image.objects.all()
    return render(request,'home.html',{"pic":pic})

def location(request):
    
    return render(request,'all-pictures/location.html')

def category(request):

    return render(request,'all-pictures/category.html')
