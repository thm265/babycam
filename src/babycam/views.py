from django.shortcuts import render
# from django.http import HttpResponse
# import RPi.GPIO as GPIO

# Create your views here.

def cam_view(request, *args, **kwargs):
    return render(request, "babycam.html",{})

def rotation_view(request, *args, **kwargs):
    a = request.POST.get('mobile-on')
    b = request.POST.get('mobile-off')
    print(a)
    print(b)
    return render(request, "rotation.html",{})

def webrtc_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "webrtc_view.html",{})