# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20170121_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=64, null=True, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba', blank=True),
        ),
    ]
