from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'qna.views.home', name='home'),
    url(r'^about/$', 'qna.views.about', name='about'),
    url(r'^q/$', 'qna.views.question', name='question'),
    url(r'^login/$', 'qna.views.login', name='login'),






    # url(r'^$', 'qna.views.home', name='home'),

)
