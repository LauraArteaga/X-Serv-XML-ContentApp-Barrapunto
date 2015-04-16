# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentAppBarrapunto', '0004_delete_out'),
    ]

    operations = [
        migrations.CreateModel(
            name='Out',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('out', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
