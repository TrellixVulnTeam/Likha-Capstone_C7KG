# Generated by Django 2.1b1 on 2018-11-08 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('causalmodel', '0029_auto_20181107_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestedintervention',
            name='reason',
            field=models.CharField(choices=[('From Strategic Planning', 'From Strategic Planning'), ('National Initiative', 'National Initiative'), ('Innovative Programs', 'Innovative Programs')], default='From Strategic Planning', max_length=200),
        ),
    ]
