# Generated by Django 4.2.1 on 2023-05-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculation',
            name='has_parent',
        ),
        migrations.AddField(
            model_name='calculation',
            name='has_father',
            field=models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='calculation',
            name='has_mother',
            field=models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='N', max_length=1),
        ),
    ]
