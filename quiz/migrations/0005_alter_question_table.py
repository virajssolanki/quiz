# Generated by Django 4.0.5 on 2022-06-22 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_rename_qustion_question_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='question',
            table='question',
        ),
    ]
