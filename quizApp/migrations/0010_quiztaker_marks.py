# Generated by Django 3.0.2 on 2021-06-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0009_auto_20210530_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiztaker',
            name='marks',
            field=models.FloatField(default=0.0),
        ),
    ]
