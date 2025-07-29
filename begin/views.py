from django.http import HttpResponse
from django.shortcuts import render #render the html file

def home(request):
    #return HttpResponse("Hello, world!")
    return render(request,'index.html')

def about(request):
    return HttpResponse("Hello, world!,this is about page")

def contact(request):
    return HttpResponse("Hello, world! this is contact page")

