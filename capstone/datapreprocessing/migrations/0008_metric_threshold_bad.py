# Generated by Django 2.1b1 on 2018-07-10 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapreprocessing', '0007_metric_is_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='threshold_bad',
            field=models.BooleanField(default=True, verbose_name='Is Value Reaching Threshold Bad'),
        ),
    ]
