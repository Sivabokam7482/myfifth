from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('THIS IS STRING OF THE FIRST FILE')

def second(request):
    return render(request,'first.html')
    