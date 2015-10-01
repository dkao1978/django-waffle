# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('waffle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='stores',
            field=models.ManyToManyField(help_text=b'Activate this flag for these stores.', to='store.Store', blank=True),
        ),
    ]
