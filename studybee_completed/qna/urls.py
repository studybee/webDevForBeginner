from django.conf.urls import patterns, url

urlpatterns = patterns(
    'qna.views',
    url(r'^question/(?P<question_id>[0-9]+)/$', 'question',
        name='view_question'),
    # url(r'^question/(?P<question_id>[0-9]/\
    #     comment/(?P<comment_id>[0-9]+)/(?P<status>up|down)/$', 'popularity',
    #     name='comment_popularity'),
    url(
        r'^question/comment/(?P<comment_id>[0-9]+)/(?P<status>up|down)/$',
        'popularity', name='comment_popularity'),
    url(r'^post/$', 'post', name='post'),
)
