# Generated by Django 4.2.1 on 2023-07-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0008_alter_calculation_number_of_brothers_from_father_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculation',
            name='father_share',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]