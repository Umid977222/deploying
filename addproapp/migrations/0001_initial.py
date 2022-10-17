# Generated by Django 4.1.2 on 2022-10-16 10:03

import addproapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('img', models.ImageField(default='posts/default.jpg', upload_to=addproapp.models.upload_location)),
                ('description', models.TextField()),
                ('add_bot_button', models.BooleanField()),
            ],
        ),
    ]
