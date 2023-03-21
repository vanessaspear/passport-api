# Generated by Django 4.1.7 on 2023-03-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passportapi', '0007_alter_trip_options_trip_latitude_trip_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='itinerary',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trip',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]