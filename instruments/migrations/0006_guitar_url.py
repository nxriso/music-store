# Generated by Django 2.1.5 on 2019-01-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0005_auto_20190129_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='url',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]