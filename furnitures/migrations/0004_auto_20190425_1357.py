# Generated by Django 2.2 on 2019-04-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures', '0003_auto_20190425_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveIntegerField(),
        ),
    ]
