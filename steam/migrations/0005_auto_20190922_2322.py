# Generated by Django 2.2.5 on 2019-09-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0004_auto_20190922_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steam',
            name='image',
            field=models.TextField(),
        ),
    ]