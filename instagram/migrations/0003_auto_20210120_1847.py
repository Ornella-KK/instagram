# Generated by Django 2.0 on 2021-01-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20210120_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
    ]
