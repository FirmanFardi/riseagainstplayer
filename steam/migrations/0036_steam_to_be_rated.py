# Generated by Django 2.2.5 on 2020-01-20 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0035_auto_20200120_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='steam',
            name='to_be_rated',
            field=models.NullBooleanField(default=False),
        ),
    ]
