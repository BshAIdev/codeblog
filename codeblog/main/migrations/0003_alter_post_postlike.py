# Generated by Django 5.1.3 on 2024-12-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_postlike_delete_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postLike',
            field=models.IntegerField(default=0),
        ),
    ]
