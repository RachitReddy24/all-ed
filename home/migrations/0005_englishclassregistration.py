# Generated by Django 3.1.13 on 2024-01-04 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_mentorshipregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishClassRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('preferred_time', models.CharField(max_length=50)),
                ('fluency_level', models.CharField(max_length=50)),
            ],
        ),
    ]
