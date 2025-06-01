from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("home page")
    return render(request, 'website/index.html')
def about(request):
    # return HttpResponse("about page")
    return render(request, 'website/about.html')

def contact(request):
    return HttpResponse("contact page")