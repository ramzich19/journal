# Generated by Django 3.1.5 on 2021-02-19 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20210219_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='document',
        ),
    ]