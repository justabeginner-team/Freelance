# Generated by Django 2.2.13 on 2020-07-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_merge_20200707_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]