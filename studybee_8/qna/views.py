from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from qna.forms import SignupForm, PostForm, CommentForm
from qna.models import Question, Tag


def question(request, question_id):
    """
    viewing the question
    """
    if int(question_id) == 0:
        HttpResponseRedirect(reverse('home'))

    q = get_object_or_404(Question, id=question_id)

    return render(request, 'question.html', {
        'question': q,
    })


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
    questions = Question.objects.order_by('-updated_at')

    # Paginator
    paginator = Paginator(questions, 1)
    current_page = request.GET.get('page')
    try:
        page = paginator.page(current_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        page = paginator.page(paginator.num_pages)

    return render(request, "index.html", {
        'questions': page,
    })


def about(request):
    return render(request, "about.html")


def question(request, question_id=0):
    """
    viewing the question
    """
    if int(question_id) == 0:
        HttpResponseRedirect(reverse('home'))

    q = get_object_or_404(Question, id=question_id)

    # Comment Form
    if request.method == "POST":
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            _comment = commentform.save(commit=False)
            _comment.user = request.user
            _comment.question = q
            _comment.save()

            return HttpResponseRedirect(reverse(
                'view_question',
                kwargs={'question_id': question_id}
            ))

    elif request.method == "GET":
        commentform = CommentForm()

    return render(request, "question.html", {
        'question': q,
        'commentform': commentform,
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

            # Tags
            for _tagname in request.POST.get('tags').split(","):
                _tagname = _tagname.strip()

                if _tagname:
                    _tag, _created = Tag.objects.get_or_create(
                        name=_tagname,
                        defaults={'name': _tagname})
                    post.tags.add(_tag)

            return HttpResponseRedirect(reverse('home'))

    elif request.method == "GET":
        postform = PostForm()

    return render(request, "post.html", {
        'postform': postform,
    })
