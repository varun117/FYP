# Generated by Django 3.0.7 on 2021-03-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210323_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visit',
            field=models.BooleanField(max_length=3),
        ),
    ]
