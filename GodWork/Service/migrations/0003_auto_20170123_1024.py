# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0002_auto_20170123_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='cpu',
            field=models.CharField(max_length=256, verbose_name=b'cpu'),
        ),
        migrations.AlterField(
            model_name='service',
            name='host',
            field=models.CharField(max_length=256, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
