# Generated by Django 4.1.3 on 2022-11-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='symbol',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]