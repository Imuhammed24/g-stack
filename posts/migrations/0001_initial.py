# Generated by Django 3.0 on 2019-12-26 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=450)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        # migrations.CreateModel(
        #     name='Images',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('image', models.ImageField(upload_to=posts.models.get_image_filename, verbose_name='Image')),
        #         ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='posts.Post')),
        #     ],
        # ),
    ]