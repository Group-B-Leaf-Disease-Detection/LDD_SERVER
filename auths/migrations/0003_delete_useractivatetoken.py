# Generated by Django 4.2.6 on 2023-11-01 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0002_useractivatetoken_delete_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserActivateToken',
        ),
    ]
