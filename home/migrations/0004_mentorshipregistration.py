# Generated by Django 3.1.13 on 2024-01-04 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20240104_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentorshipregistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('one_on_one_sessions', models.BooleanField(default=False)),
                ('personalized_guidance', models.BooleanField(default=False)),
                ('skill_development_workshops', models.BooleanField(default=False)),
            ],
        ),
    ]
