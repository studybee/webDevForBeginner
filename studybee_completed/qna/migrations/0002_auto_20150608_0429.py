# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-popularity', '-updated_at'], 'get_latest_by': 'updated_at'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AddField(
            model_name='comment',
            name='popularity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=80, blank=True),
        ),
    ]
