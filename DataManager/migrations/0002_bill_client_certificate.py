# Generated by Django 3.0.8 on 2020-09-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='client_certificate',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
