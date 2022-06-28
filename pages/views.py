# pages/views.py
from django.shortcuts import HttpResponse,render


def homePageView(request):
    return render(request,'idx.html')