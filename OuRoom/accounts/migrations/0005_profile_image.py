# Generated by Django 4.2.7 on 2024-02-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_birth_date_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='userdef.jpg', upload_to='profile_pics'),
        ),
    ]
