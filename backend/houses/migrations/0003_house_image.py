# Generated by Django 3.0.7 on 2020-06-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20200619_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]