# Generated by Django 3.2.6 on 2021-08-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0005_message_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
