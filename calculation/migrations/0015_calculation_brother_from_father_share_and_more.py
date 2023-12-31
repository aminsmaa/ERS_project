# Generated by Django 4.2.1 on 2023-08-03 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0014_calculation_father_of_father_share_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculation',
            name='brother_from_father_share',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='calculation',
            name='brother_from_mother_share',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='calculation',
            name='sister_from_father_share',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='calculation',
            name='sister_from_mother_share',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
