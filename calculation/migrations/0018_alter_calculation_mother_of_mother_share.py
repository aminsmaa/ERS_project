# Generated by Django 4.2.1 on 2023-08-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0017_alter_calculation_mother_of_mother_share'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='mother_of_mother_share',
            field=models.FloatField(default=0.0),
        ),
    ]