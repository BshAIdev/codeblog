# Generated by Django 5.1.3 on 2024-12-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_postlike'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postView',
            field=models.IntegerField(default=0),
        ),
    ]
