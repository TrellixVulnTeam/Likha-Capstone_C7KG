# Generated by Django 2.1b1 on 2018-07-01 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('causalmodel', '0006_causalmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='causal_model',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='causalmodel.CausalModel'),
        ),
    ]
