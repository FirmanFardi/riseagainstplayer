# Generated by Django 2.2.5 on 2020-01-19 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0033_auto_20200116_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steam',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.Rating'),
        ),
    ]