# Generated by Django 4.0.5 on 2022-06-21 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='full name'),
        ),
    ]
