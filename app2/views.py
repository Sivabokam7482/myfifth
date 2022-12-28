from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def third(request):
    return HttpResponse('<h1><i>this is third file</h1></i>')

def forth(request):
    return render(request,'second.html')
    