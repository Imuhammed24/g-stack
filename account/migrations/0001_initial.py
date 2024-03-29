# Generated by Django 3.0 on 2019-12-21 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('profile_photo', models.ImageField(blank=True, upload_to='profile_pictures/')),
                ('bio', models.TextField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('institute', models.CharField(blank=True, max_length=100)),
                ('nationality', models.CharField(blank=True, max_length=25)),
                ('discipline', models.CharField(blank=True, max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
