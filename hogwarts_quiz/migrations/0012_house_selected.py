# Generated by Django 3.2.9 on 2021-11-21 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hogwarts_quiz', '0011_remove_result_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='selected',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
