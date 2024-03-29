# Generated by Django 3.0.7 on 2021-03-23 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20210323_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(default='Male', max_length=10)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('Birthday', models.DateField(default=django.utils.timezone.now)),
                ('visit', models.BooleanField(default=None)),
                ('reason', models.CharField(blank=True, max_length=200)),
                ('scanned_pic', models.ImageField(upload_to='scanned_pic/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userinfo')),
            ],
        ),
    ]
