# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0003_remove_question_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='popularity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
