# Generated by Django 2.0.2 on 2019-05-31 19:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('slug', models.CharField(editable=False, max_length=500)),
                ('owner', models.ForeignKey(editable=False, on_delete='DO_NOTHING', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
                ('slug', models.SlugField(editable=False, max_length=500)),
                ('blog', models.ForeignKey(on_delete='DO_NOTHING', to='blog.Blog')),
            ],
        ),
    ]
