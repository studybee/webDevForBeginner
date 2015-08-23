# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0002_auto_20150608_0429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='subtitle',
        ),
    ]
