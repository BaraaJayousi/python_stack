# Generated by Django 5.0.2 on 2024-03-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
