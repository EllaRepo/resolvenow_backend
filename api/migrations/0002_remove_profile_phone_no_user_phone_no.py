# Generated by Django 4.2.6 on 2023-11-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
