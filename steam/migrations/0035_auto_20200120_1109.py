# Generated by Django 2.2.5 on 2020-01-20 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0034_auto_20200119_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steam',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
