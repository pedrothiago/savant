# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_iteminproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteminproject',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
