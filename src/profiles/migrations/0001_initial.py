# Generated by Django 3.0.5 on 2021-04-08 11:54

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
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('bio', models.TextField(default='Enter your bio', max_length=300)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('avatar', models.ImageField(default='avatar.png', upload_to='avatars/')),
                ('slug', models.SlugField(unique=True)),
                ('update_on', models.DateTimeField(auto_now=True)),
                ('create_on', models.DateTimeField(auto_now=True)),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]