# Generated by Django 2.2.5 on 2019-12-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0027_steam_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steam',
            name='gametitle',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='steam',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='steam',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
