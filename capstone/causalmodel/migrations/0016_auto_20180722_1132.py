# Generated by Django 2.1b1 on 2018-07-22 03:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('causalmodel', '0015_auto_20180721_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='CausalModelComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('causal_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='causalmodel.CausalModel')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='causalmodelcomments',
            name='causal_model',
        ),
        migrations.RemoveField(
            model_name='causalmodelcomments',
            name='profile',
        ),
        migrations.DeleteModel(
            name='CausalModelComments',
        ),
    ]
