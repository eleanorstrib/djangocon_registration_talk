# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20160717_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='story',
            field=models.CharField(choices=[('cinderella', 'Cinderella'), ('hansel_gretel', 'Hansel & Gretel'), ('rapunzel', 'Rapunzel'), ('snow_white', 'Snow White and the Seven Dwarfs'), ('three_pigs', 'Three Little Pigs'), ('twelve_princesses', 'Twelve Dancing Princesses')], max_length=100),
        ),
    ]