# Generated by Django 3.2.9 on 2021-11-20 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hogwarts_quiz', '0010_auto_20211120_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='comment',
        ),
    ]