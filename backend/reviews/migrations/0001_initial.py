# Generated by Django 3.0.7 on 2020-08-30 16:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now=True)),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='houses.House')),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='reservations.Reservation')),
            ],
        ),
    ]
