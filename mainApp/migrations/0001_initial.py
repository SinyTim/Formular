# Generated by Django 2.1 on 2018-08-18 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='mainApp/posts_img')),
            ],
        ),
    ]