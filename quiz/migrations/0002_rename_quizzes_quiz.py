# Generated by Django 3.2.8 on 2021-10-29 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quizzes',
            new_name='Quiz',
        ),
    ]
