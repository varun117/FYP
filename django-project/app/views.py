from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .models import *

from PIL import Image
import numpy as np
from .FinalScript import *
# Create your views here.

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create(username = email, first_name = first_name, last_name = last_name, email = email)
        print("user object is created")
        user.password = make_password(password)
        user.save()
        print("password changed succesfully")
        userinfo.objects.create(user = user)
        print("userinfo is added")
        return HttpResponseRedirect(reverse('app:home',args=(user.id,)))
    return render(request,'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username ,password=password)
        if user:
            login(request,user)
            print("User has logged in")
            return HttpResponseRedirect(reverse('app:home',args=(user.id,)))
        else:
            print("wrong details")
            return render(request, 'signup.html',{'alert_flag': True})
    return render(request,'signup.html')


def home(request,pk):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        birthday = request.POST.get('birthday')
        visit = request.POST.get('visit')
        date = request.POST.get('date')
        time = request.POST.get('time')
        image = request.FILES['image']
        reason = request.POST.get('body')
        user = User.objects.get(pk = pk)
        user_info = userinfo.objects.get(user = user)
        Post.objects.create(user = user, user_info = user_info , gender = gender , address = address , phone = phone , birthday = birthday, visit = visit, date = date, time = time, scanned_pic = image, reason = reason)
        print("userinfo is added")
        if first_name and last_name and phone and image:
            return HttpResponseRedirect(reverse('app:home',args=(user.id,)))
    return render(request ,'home.html')

#On submit, storing the file and displaying the loading screen
def submit(request):
    context = None
    if request.method == 'POST' and request.FILES['image']:
        context = dict()
        CXRimage = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(request.POST.get('first_name')+'-'+request.POST.get('last_name')+'-'+request.POST.get('phone')+'-'+CXRimage.name, CXRimage)
        uploaded_file_url = fs.url(filename)
        context['first_name'] = request.POST.get('first_name')
        context['last_name'] = request.POST.get('last_name')
        context['uploadedURL'] = uploaded_file_url
    return render(request, 'result.html', context)

#Processing data in the background and returning an asynchronous Json response
def process_data(request):
    print("Processing data...")
    context = dict()
    context['fname'] = request.POST.get('fname')
    context['lname'] = request.POST.get('lname')
    context['results'] = testForImage(request.POST.get('uploaded_file_url'))
    context['covidFlag'] = 'True' if context['results']=="Infected" else 'False'
    return JsonResponse(context)
