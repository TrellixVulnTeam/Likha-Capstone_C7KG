# Generated by Django 2.1b1 on 2018-07-30 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datainput', '0026_auto_20180712_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='childcare',
            name='dengue',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5, verbose_name='Number of Dengue Cases'),
        ),
        migrations.AddField(
            model_name='childcare',
            name='hepatitis',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5, verbose_name='Number of Children with Hepatitis'),
        ),
        migrations.AddField(
            model_name='childcare',
            name='measles',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5, verbose_name='Number of Children with Measles'),
        ),
        migrations.AddField(
            model_name='maternalcare',
            name='low_birth_weight',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='Number of mothers who have children with low birth weight'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maternalcare',
            name='practicing_ebf',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=5, verbose_name='Number of mothers practicing exclusive breastfeeding'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='childcare',
            name='anemic_children',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Anemic children'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='anemic_children_with_iron',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Anemic children receiving full dose iron'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='diarrhea_cases',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Diarrhea cases'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='pneumonia_cases',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Pneumonia cases'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='received_MNP',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of children who received MNP'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='received_iron',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of children who received iron'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='received_vitamin_A',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of children who received vitamin A'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='sick_children',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Sick children'),
        ),
        migrations.AlterField(
            model_name='immunization',
            name='given_bcg',
            field=models.IntegerField(verbose_name='Number of Children Given BCG'),
        ),
        migrations.AlterField(
            model_name='immunization',
            name='given_hepa',
            field=models.IntegerField(verbose_name='Number of Children Given HEPA'),
        ),
        migrations.AlterField(
            model_name='immunization',
            name='given_mcv',
            field=models.IntegerField(verbose_name='Number of Children Given MCV'),
        ),
        migrations.AlterField(
            model_name='immunization',
            name='given_opv',
            field=models.IntegerField(verbose_name='Number of Children Given OPV'),
        ),
        migrations.AlterField(
            model_name='immunization',
            name='given_pcv',
            field=models.IntegerField(verbose_name='Number of Children Given PCV'),
        ),
        migrations.AlterField(
            model_name='immunization',
            name='given_penta',
            field=models.IntegerField(verbose_name='Number of Children Given PENTA'),
        ),
        migrations.AlterField(
            model_name='immunization',
            name='given_rota',
            field=models.IntegerField(verbose_name='Number of Children Given ROTA'),
        ),
        migrations.AlterField(
            model_name='malaria',
            name='malaria_cases',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Malaria Cases'),
        ),
        migrations.AlterField(
            model_name='maternalcare',
            name='breastfed',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Postpartum women initiated breastfeeding within 1 hour after delivery'),
        ),
        migrations.AlterField(
            model_name='maternalcare',
            name='complete_iron',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Pregnant women given complete iron with folic acid supplementation'),
        ),
        migrations.AlterField(
            model_name='maternalcare',
            name='complete_iron_post',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Postpartum women with given complete iron supplementation'),
        ),
        migrations.AlterField(
            model_name='maternalcare',
            name='postpartum_visits',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Postpartum women with at least 2 postpartum visits'),
        ),
        migrations.AlterField(
            model_name='maternalcare',
            name='prenatal_visits',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Pregnant women with 4 or more prenatal visits'),
        ),
        migrations.AlterField(
            model_name='maternalcare',
            name='tetanus_toxoid',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Pregnant women given 2 doses of Tetanus Toxoid'),
        ),
        migrations.AlterField(
            model_name='maternalcare',
            name='tt2_plus',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Pregnant women given TT2 plus'),
        ),
        migrations.AlterField(
            model_name='maternalcare',
            name='vitamin_a',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Postpartum women given Vitamin A supplementation'),
        ),
        migrations.AlterField(
            model_name='tuberculosis',
            name='identified',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Number of Tuberculosis Identified'),
        ),
    ]
