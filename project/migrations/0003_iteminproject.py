# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20160615_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemInProject',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date_debit', models.DateField()),
                ('item', models.ForeignKey(to='project.AccountingItem')),
                ('project', models.ForeignKey(to='project.Project')),
            ],
        ),
    ]
