# Generated by Django 4.0.5 on 2022-06-22 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_qustion_option_a_remove_qustion_option_b_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='option',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='option'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='qustion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mcqs', to='quiz.qustion'),
        ),
    ]