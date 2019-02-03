# Generated by Django 2.1.5 on 2019-02-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0008_remove_guitar_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]