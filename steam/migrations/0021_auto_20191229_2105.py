# Generated by Django 2.2.5 on 2019-12-29 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('steam', '0020_auto_20191229_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='steam',
            name='tag',
        ),
        migrations.AddField(
            model_name='steam',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag'),
        ),
        migrations.AlterField(
            model_name='steam',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developer.Developer'),
        ),
    ]