from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from qna.forms import LoginForm

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', 'qna.views.signup', name='signup'),
    url(r'^signup_ok/$', TemplateView.as_view(
        template_name='registration/signup_ok.html'
    ), name='signup_ok'),

    url(r'^$', 'qna.views.home', name='home'),
    url(r'^about/$', 'qna.views.about', name='about'),
    url(r'^q/$', 'qna.views.question', name='question'),
    url(r'^post/$', 'qna.views.post', name='post'),

    url(r'^login/$', 'django.contrib.auth.views.login', {
        'authentication_form': LoginForm
    }, name='login_url'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/login/',
    }, name='logout_url'),

    (r'^summernote/', include('django_summernote.urls')),
)
