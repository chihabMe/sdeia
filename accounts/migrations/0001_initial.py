# Generated by Django 3.2.10 on 2022-03-26 16:32

import accounts.models
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to=accounts.models.namer)),
                ('blocked_users', models.ManyToManyField(related_name='user_blocked', to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(related_name='user_followers', to=settings.AUTH_USER_MODEL)),
                ('follwing', models.ManyToManyField(related_name='user_follwing', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='user_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
