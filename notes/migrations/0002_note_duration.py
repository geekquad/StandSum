# Generated by Django 3.1.3 on 2020-12-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='duration',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
