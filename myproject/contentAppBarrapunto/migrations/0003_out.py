# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentAppBarrapunto', '0002_auto_20150415_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Out',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('out', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
