# Generated by Django 3.2.3 on 2021-05-26 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0002_auto_20210526_2054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['name'], 'verbose_name_plural': 'quizes'},
        ),
    ]