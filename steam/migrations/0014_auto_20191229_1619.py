# Generated by Django 2.2.5 on 2019-12-29 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0013_auto_20191229_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steam',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genre.Genre'),
        ),
    ]
