from django.shortcuts import render
from .forms import AgentForm

# Create your views here.
def frontpage(request):
    return render(request, "sim/index.html")

def python(request):
    return render(request, "sim/python.html")

def photo(request):
    return render(request, "sim/Photo.html")

def agents(request):
    return render(request, "sim/python.html", {"form":AgentForm})
