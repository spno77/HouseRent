# Generated by Django 3.0.7 on 2020-07-28 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houses', '0003_auto_20200725_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('days', models.IntegerField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house', to='houses.House')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]