from django.db import models
from django.conf import settings


class Question(models.Model):
    """question
    when a user posts questions
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=300)
    content = models.TextField()
    tags = models.ManyToManyField('Tag')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at']

    def __unicode__(self):
        return u"{0}".format(self.title)


class Comment(models.Model):
    """comments
    comments in one question
    """
    question = models.ForeignKey(Question)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    popularity = models.PositiveIntegerField(default=0)
    content = models.TextField(max_length=600)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-popularity', '-created_at']
        get_latest_by = 'created_at'

    def __unicode__(self):
        return u'Q: {0} - Comment: {1}'.format(self.question.id, self.id)


class Tag(models.Model):
    """Tag
    Tag in question
    """
    name = models.CharField(max_length=80, blank=True)

    def __unicode__(self):
        return u"{0}".format(self.name)
