from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from qna.forms import SignupForm, PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from qna.models import Question, Tag, Comment


def home(request, tag=None):
    """home
    to view top articles
    """
    # Pagination
    if tag is None:
        questions = Question.objects.order_by('-updated_at')
    else:
        questions = Question.objects.filter(
            tags__in=Tag.objects.filter(name=tag)
            ).order_by('-updated_at')

    paginator = Paginator(questions, 5)
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


def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['eamil']
            user.save()

            return HttpResponseRedirect(
                reverse("signup_ok")
            )
    elif request.method == "GET":
        signupform = SignupForm()

    return render(request, "registration/signup.html", {
        "signupform": signupform,
    })


@login_required
def post(request):
    """
    posting questions
    """
    if request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            _post = postform.save(commit=False)
            _post.user = request.user
            _post.save()

            # tags(ManyToManyField)
            for _tagname in request.POST.get('tags', '').split(','):
                _tagname = _tagname.strip()

                # When only _tagname is not blank
                if _tagname:
                    _tag, _created = Tag.objects.get_or_create(
                        name=_tagname, defaults={'name': _tagname})
                    _post.tags.add(_tag)

            return HttpResponseRedirect(reverse('home'))
    elif request.method == "GET":
        postform = PostForm()

    return render(request, "post.html", {
        'postform': postform,
    })


def question(request, question_id=0):
    """
    viewing the question
    """
    if int(question_id) == 0:
        HttpResponseRedirect(reverse('home'))

    q = get_object_or_404(Question, id=question_id)

    # Comment Form
    if request.method == "POST":
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('login_url'))

        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            _commentform = commentform.save(commit=False)
            _commentform.question = q
            _commentform.user = request.user
            _commentform.save()

            return HttpResponseRedirect(
                reverse(
                    'view_question',
                    kwargs={'question_id': question_id}))
    elif request.method == "GET":
        commentform = CommentForm()

    return render(request, "question.html", {
        'question': q,
        'commentform': commentform,
    })


@login_required
def popularity(request, comment_id=0, status=None):
    """
    to higher or lower popularity of the comment.
    """
    if int(comment_id) == 0 or status is None:
        HttpResponseRedirect(reverse('home'))

    status = status.lower()
    c = get_object_or_404(Comment, id=comment_id)

    if status == "up":
        c.popularity += 1
    elif status == "down":
        if c.popularity == 0:
            pass
        else:
            c.popularity -= 1

    c.save()

    return HttpResponseRedirect(reverse(
            'view_question',
            kwargs={'question_id': c.question.id}))
