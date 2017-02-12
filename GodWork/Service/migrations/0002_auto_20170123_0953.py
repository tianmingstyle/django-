# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='cpu',
            field=models.CharField(max_length=128, verbose_name=b'cpu'),
        ),
        migrations.AlterField(
            model_name='service',
            name='disk',
            field=models.CharField(max_length=128, verbose_name=b'\xe7\xa1\xac\xe7\x9b\x98'),
        ),
        migrations.AlterField(
            model_name='service',
            name='host',
            field=models.CharField(max_length=128, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='service',
            name='ip',
            field=models.CharField(max_length=128, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xbaip'),
        ),
        migrations.AlterField(
            model_name='service',
            name='mac',
            field=models.CharField(max_length=128, verbose_name=b'mac'),
        ),
        migrations.AlterField(
            model_name='service',
            name='mem',
            field=models.CharField(max_length=128, verbose_name=b'\xe5\x86\x85\xe5\xad\x98'),
        ),
        migrations.AlterField(
            model_name='service',
            name='model',
            field=models.CharField(max_length=128, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x9e\x8b\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='service',
            name='system',
            field=models.CharField(max_length=128, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f'),
        ),
    ]
