# Generated by Django 2.2.5 on 2019-09-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0004_scraper_url1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scraper',
            name='image1',
            field=models.ImageField(default='', editable=False, upload_to='profile_pics'),
        ),
    ]