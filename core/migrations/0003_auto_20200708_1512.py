# Generated by Django 2.2.13 on 2020-07-08 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200705_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('new', 'new'), ('best rated', 'best rated'), ('best seller', 'best seller')], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.ManyToManyField(related_name='items', to='core.Label'),
        ),
    ]