# Generated by Django 3.2.8 on 2021-10-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='nickname',
            field=models.CharField(default=5, max_length=20),
            preserve_default=False,
        ),
    ]
