# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-25 19:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peer_review', '0004_auto_20161220_1955'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PeerReviewAssignment',
        ),
        migrations.DeleteModel(
            name='PeerReviewAssignmentArticleResponses',
        ),
        migrations.DeleteModel(
            name='PeerReviewAssignmentArticleResponseSettings',
        ),
        migrations.DeleteModel(
            name='PeerReviewAssignmentDenied',
        ),
        migrations.DeleteModel(
            name='PeerReviewAssignmentEssays',
        ),
        migrations.DeleteModel(
            name='PeerReviewAssignmentEssaySettings',
        ),
        migrations.DeleteModel(
            name='PeerReviewAssignmentImages',
        ),
        migrations.DeleteModel(
            name='PeerReviewAssignmentIndependent',
        ),
    ]