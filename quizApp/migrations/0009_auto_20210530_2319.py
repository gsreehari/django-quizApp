# Generated by Django 3.0.2 on 2021-05-30 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0008_auto_20210530_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answerMarks',
        ),
        migrations.AddField(
            model_name='question',
            name='questionMarks',
            field=models.IntegerField(default=1),
        ),
    ]
