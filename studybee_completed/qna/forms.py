from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from qna.models import Question, Comment

from django_summernote.widgets import SummernoteWidget


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(SignupForm, self).__init__(*args, **kwargs)

    username = forms.RegexField(
        max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': "This value may contain only letters, numbers and "
                         "@/./+/-/_ characters."
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'required': 'True',
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': 'True',
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
                'required': 'True',
            }
        ),
        help_text="Enter the same password as above, for verification."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

    def save(self, commit=True):
        _user = super(UserCreationForm, self).save(commit=False)
        _user.email = self.cleaned_data['email']
        _user.set_password(self.cleaned_data['password1'])
        if commit:
            _user.save()
        return _user


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        # Set the label to omit ':'
        kwargs.setdefault('label_suffix', '')

        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PostForm, self).__init__(*args, **kwargs)

    title = forms.CharField(
        required=True,
        max_length=300,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                }
            )
        )
    content = forms.CharField(
        widget=SummernoteWidget(
            attrs={
                'placeholder': 'Content',
            }
        )
    )
    tags = forms.CharField(
        label='Tag',
        required=False,
        max_length=200,
        help_text=u"Tags are separated by comma(,).",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Question
        fields = ('title', 'content', 'tags',)


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CommentForm, self).__init__(*args, **kwargs)

    content = forms.CharField(
        label='Comment',
        required=False,
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Comment',
                'rows': '3',
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('content',)
