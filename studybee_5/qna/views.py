from django.shortcuts import render

# Create your views here.
def home(request, tag=None):
    return render(request, "index.html")

def about(request, tag=None):
    return render(request, "about.html")

def question(request, tag=None):
    return render(request, "question.html")

def login(request, tag=None):
    return render(request, "login.html")