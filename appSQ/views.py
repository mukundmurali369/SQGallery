from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def internship(request):
    return render(request,'internship.html')

def civilworks(request):
    return render(request,'civilworks.html')

def gallery(request):
    return render(request,'gallery.html')

def contactus(request):
    return render(request,'contactus.html')

def work_updates(request):
    return render(request,'workupdates.html')

def our_products(request):
    return render(request,'our_products.html')

def addtocart(request):
    return render(request,'addtocart.html')

def checkout(request):
    return render(request,'checkout.html')

def ButabondSBR_moreinfo(request):
    return render(request,'ButabondSBR_moreinfo.html')