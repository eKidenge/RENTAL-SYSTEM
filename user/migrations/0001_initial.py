# Generated by Django 3.1.2 on 2021-01-03 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('dimention', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('kitchen', models.CharField(max_length=3)),
                ('hall', models.CharField(max_length=3)),
                ('balcany', models.CharField(max_length=3)),
                ('desc', models.CharField(max_length=200)),
                ('AC', models.CharField(max_length=3)),
                ('img', models.ImageField(upload_to='room_id/')),
                ('date', models.DateField(auto_now=True)),
                ('user_email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('house_id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('kitchen', models.IntegerField()),
                ('hall', models.CharField(max_length=3)),
                ('balcany', models.CharField(max_length=3)),
                ('desc', models.CharField(max_length=200)),
                ('AC', models.CharField(max_length=3)),
                ('img', models.ImageField(upload_to='house_id/')),
                ('date', models.DateField(auto_now=True)),
                ('user_email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
