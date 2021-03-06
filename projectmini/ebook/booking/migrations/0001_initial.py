# Generated by Django 3.0.3 on 2020-03-05 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('open_time', models.TimeField(verbose_name='')),
                ('close_time', models.TimeField(verbose_name='')),
                ('capacity', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField(verbose_name='')),
                ('end_time', models.TimeField(verbose_name='')),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('status_remark', models.BooleanField(default=False)),
                ('bookdate', models.DateField()),
                ('bookby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.User')),
                ('roomid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Room')),
            ],
        ),
    ]
