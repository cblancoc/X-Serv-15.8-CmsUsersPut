# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_users_put', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='name',
            new_name='blog',
        ),
        migrations.RemoveField(
            model_name='table',
            name='number',
        ),
        migrations.AddField(
            model_name='table',
            name='url',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
