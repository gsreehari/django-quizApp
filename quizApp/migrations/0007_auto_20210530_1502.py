# Generated by Django 3.0.2 on 2021-05-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0006_auto_20210530_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answerMarks',
            field=models.IntegerField(default=1),
        ),
    ]
