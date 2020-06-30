# Generated by Django 2.2.13 on 2020-06-30 07:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200624_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='rating',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=10),
        ),
        migrations.AddField(
            model_name='rating',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='rating',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='7SrfT7elC8Xl5PTl', unique=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='core.Item'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='rating',
            name='stars',
        ),
    ]
