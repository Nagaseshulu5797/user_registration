from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def register(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            usud=ufd.save(commit=False)
            usud.set_password(ufd.cleaned_data['password'])
            usud.save()

            uspd=pfd.save(commit=False)
            uspd.username=usud
            uspd.save()
            return HttpResponse('register is successfully')
        else:
            return HttpResponse('data is not valid')
    return render(request,'register.html',d)
def home(request):
    
    return render(request,'home.html')

