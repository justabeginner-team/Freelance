# Generated by Django 2.2.13 on 2020-06-08 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200608_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]