# Generated by Django 5.1.3 on 2024-12-11 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postCom',
            field=models.IntegerField(default=0),
        ),
    ]
