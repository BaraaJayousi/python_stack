# Generated by Django 5.0.2 on 2024-03-09 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninja_app', '0002_dojos_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default='old dojo', max_length=255),
        ),
    ]