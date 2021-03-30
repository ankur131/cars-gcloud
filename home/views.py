from django.shortcuts import render, HttpResponse
from datetime import datetime
#from home.models import Contact
from django.contrib import messages

# Create your views here.



def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")


# below are not required for now
def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')


