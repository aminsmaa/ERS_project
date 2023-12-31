# Generated by Django 4.2.1 on 2023-05-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0003_alter_calculation_singularity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='number_of_brothers_from_father',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='number_of_brothers_from_mother',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='number_of_common_brothers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='number_of_common_sisters',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='number_of_daughters',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='number_of_sister_from_father',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='number_of_sisters_from_mother',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='number_of_sons',
            field=models.IntegerField(default=0),
        ),
    ]
