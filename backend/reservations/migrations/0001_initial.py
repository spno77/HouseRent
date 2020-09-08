# Generated by Django 3.0.7 on 2020-09-08 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('reserve_in', models.DateField()),
                ('reserve_out', models.DateField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house', to='houses.House')),
            ],
        ),
    ]
