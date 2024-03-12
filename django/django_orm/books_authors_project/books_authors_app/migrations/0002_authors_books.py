# Generated by Django 5.0.2 on 2024-03-10 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='books_authors_app.books'),
        ),
    ]