# Generated by Django 2.2.1 on 2021-11-11 13:48

import albums.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='name', null=True)),
                ('description', models.TextField(blank=True, default='mail', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=albums.models.upload_location)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
