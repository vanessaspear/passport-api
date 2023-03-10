# Generated by Django 4.1.7 on 2023-03-10 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('itinerary_description', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('city', models.CharField(max_length=50)),
                ('state_or_country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itinerary_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SitePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='TravelReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_reason', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state_or_country', models.CharField(max_length=50)),
                ('departure_date', models.DateField()),
                ('return_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TripReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reason', to='passportapi.travelreason')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip', to='passportapi.trip')),
            ],
        ),
        migrations.CreateModel(
            name='TripPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_photos', to='passportapi.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_photos_uploaded', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TripNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_note', models.CharField(max_length=500)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='passportapi.trip')),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_reasons',
            field=models.ManyToManyField(through='passportapi.TripReason', to='passportapi.travelreason'),
        ),
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planned_trips', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PackingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_to_pack', to='passportapi.trip')),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryPurpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary', to='passportapi.itinerary')),
                ('itinerary_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='passportapi.itinerarycategory')),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary_photos', to='passportapi.itinerary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary_photos_uploaded', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='itinerary',
            name='itinerary_purposes',
            field=models.ManyToManyField(through='passportapi.ItineraryPurpose', to='passportapi.itinerarycategory'),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_itineraries', to='passportapi.trip'),
        ),
    ]