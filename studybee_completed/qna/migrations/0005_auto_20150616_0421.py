# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0004_auto_20150610_1003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-popularity', '-created_at'], 'get_latest_by': 'created_at'},
        ),
    ]
