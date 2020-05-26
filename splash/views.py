from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def home(request):
    pic = Image.objects.all()
    return render(request,'all-pictures/home.html',{"pic":pic})

def search_location(request):
    location = Image.filter_by_location(search_term)
    message = f"{search_term}"
    return render(request,'all-pictures/location.html',{'message':message,"images":location})

def category(request):

    return render(request,'all-pictures/category.html')

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_image(search_term)
        print(searched_image)
        message = f"{search_term}"

        return render(request,'all-pictures/search.html',{"message":message,"image": searched_image})
    
    else:
        message = "You haven't searched for any term"    
       
        return render(request,'all-pictures/search.html',{"message":message})