# Generated by Django 2.2.5 on 2019-09-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0006_auto_20190922_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steam',
            name='tag',
            field=models.CharField(max_length=120),
        ),
    ]