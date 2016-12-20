# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-20 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer_review', '0003_auto_20161219_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peerreviewassignmentarticleresponsesettings',
            name='assignmentid',
            field=models.IntegerField(db_column='assignmentID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='peerreviewassignmentinstructorreviewtouchtimes',
            name='instructorid',
            field=models.IntegerField(db_column='instructorID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='peerreviewassignmentradiooptions',
            name='questionid',
            field=models.IntegerField(db_column='questionID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='peerreviewassignmentreviewanswers',
            name='questionid',
            field=models.IntegerField(db_column='questionID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='peerreviewassignmentreviewanswersdrafts',
            name='questionid',
            field=models.IntegerField(db_column='questionID', primary_key=True),
        ),
    ]
