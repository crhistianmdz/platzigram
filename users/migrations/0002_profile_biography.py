# Generated by Django 3.0.8 on 2021-03-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
