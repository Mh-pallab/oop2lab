from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Contact, Service
# Create your views here.

def home(request):
    return render(request,'home.html')
def service(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        device=request.POST.get('device')
        address=request.POST.get('address')
        problem=request.POST.get('message')

        service=Service()
        service.name=name
        service.email=email
        service.phone=phone
        service.device=device
        service.address=address
        service.problem=problem
        service.save()
        return HttpResponse('<h2>Thank you. Our service man will reach you as soon as possible</h2>')

    return render(request,'service.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        contact=Contact()
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        return HttpResponse('<h2>Thank you for contact with us</h2>')

    return render(request,'contact.html')