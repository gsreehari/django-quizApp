# Generated by Django 3.0.2 on 2021-05-30 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0005_answer_answermark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answerMark',
            new_name='answerMarks',
        ),
    ]