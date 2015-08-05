from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from qna.forms import SignupForm

def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            user.save()

            return HttpResponseRedirect(
                reverse("signup_ok")
            )
    elif request.method == "GET":
        signupform = SignupForm()

    return render(request, "registration/signup.html", {
        "signupform": signupform,
    })

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def question(request):
    return render(request, "question.html")

def login(request):
    return render(request, "registration/login.html")
