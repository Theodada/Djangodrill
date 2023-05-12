from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("<h1>hello world</h1>")

def index(request):
    return render(request, 'Todos.html')

def TODOdetail(request):
    return render(request, 'TODOdetail.html')
