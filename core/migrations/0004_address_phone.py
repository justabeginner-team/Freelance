# Generated by Django 2.2.13 on 2020-07-07 16:35

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
