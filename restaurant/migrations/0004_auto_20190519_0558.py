# Generated by Django 2.1.7 on 2019-05-19 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20190519_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
