# Generated by Django 2.2.5 on 2019-09-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scraper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gametitle', models.CharField(max_length=120)),
                ('price', models.CharField(max_length=120)),
                ('image', models.TextField()),
                ('tag', models.ImageField(upload_to='')),
                ('url', models.TextField()),
            ],
        ),
    ]