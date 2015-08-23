from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """
    Tag
    """
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    """question
    when a user posts questions
    """
    user = models.ForeignKey(User)
    tags = models.ManyToManyField('Tag')
    title = models.CharField(max_length=300)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at']

    def __unicode__(self):
        return u"{0}".format(self.title)


class Comment(models.Model):
    """
    comments in one question
    """
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    popularity = models.PositiveIntegerField(default=0)
    content = models.TextField(max_length=600)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-popularity', '-created_at']

    def __unicode__(self):
        return u'Q: {0} - Comment: {1}'.format(self.question.id, self.id)
