# Generated by Django 3.0.2 on 2021-06-02 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0012_auto_20210602_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='isPassMarks',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='questionsSwap',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='scoreToPass',
        ),
    ]
