# Generated by Django 4.0.3 on 2022-04-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220326_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
