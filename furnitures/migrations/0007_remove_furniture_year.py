# Generated by Django 2.2 on 2019-04-27 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures', '0006_delete_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furniture',
            name='year',
        ),
    ]
