from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from qna.forms import SignupForm, PostForm
from django.contrib.auth.decorators import login_required
from qna.models import Question

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

def question(request, question_id=0):
    """
    viewing the question
    """
    if int(question_id) == 0:
        HttpResponseRedirect(reverse('home'))

    q = get_object_or_404(Question, id=question_id)

    return render(request, "question.html", {
        'question': q,
    })

@login_required
def post(request):
    """
    posting questions
    """
    if request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.user = request.user
            post.save()

            return HttpResponseRedirect(reverse('home'))

    elif request.method == "GET":
        postform = PostForm()

    return render(request, "post.html", {
        'postform': postform,
    })
