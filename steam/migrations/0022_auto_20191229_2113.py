# Generated by Django 2.2.5 on 2019-12-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0021_auto_20191229_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steam',
            name='tags',
            field=models.ManyToManyField(null=True, to='tag.Tag'),
        ),
    ]