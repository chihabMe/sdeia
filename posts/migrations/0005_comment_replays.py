# Generated by Django 4.0.3 on 2022-04-08 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replays',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_replays', to='posts.comment'),
        ),
    ]
