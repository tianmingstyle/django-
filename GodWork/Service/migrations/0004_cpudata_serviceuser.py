# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0003_auto_20170123_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='CpuData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serviceid', models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8id')),
                ('cpuload', models.IntegerField(verbose_name=b'cpu\xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87')),
                ('time', models.DateTimeField(verbose_name=b'\xe7\x9b\x91\xe6\x8e\xa7\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serviceid', models.IntegerField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8id')),
                ('serviceUsername', models.CharField(max_length=128, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('servecePasswd', models.CharField(max_length=128, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81')),
            ],
        ),
    ]
