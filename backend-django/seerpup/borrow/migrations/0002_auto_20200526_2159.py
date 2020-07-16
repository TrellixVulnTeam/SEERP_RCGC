# Generated by Django 3.0.6 on 2020-05-26 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='borrow',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
