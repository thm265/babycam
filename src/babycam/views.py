from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cam_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "babycam.html",{})

def webrtc_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "webrtc_view.html",{})