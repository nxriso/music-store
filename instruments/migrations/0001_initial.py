# Generated by Django 2.1.5 on 2019-01-23 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='brands/images')),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=255)),
                ('guitar_type', models.CharField(choices=[('electric', 'Electric'), ('acoustic', 'Acoustic')], default='electric', max_length=8)),
                ('djent', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='guitars/images')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruments.Brand')),
            ],
        ),
    ]
