# Generated by Django 3.2.9 on 2021-11-21 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hogwarts_quiz', '0015_alter_house_satisfaction_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='satisfaction_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
