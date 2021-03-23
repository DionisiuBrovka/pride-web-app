# Generated by Django 3.1.7 on 2021-03-16 09:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20210310_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='preview',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 16, 9, 21, 11, 467401, tzinfo=utc), verbose_name='Дата приёма на работу'),
        ),
        migrations.AlterField(
            model_name='session',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 11, 469932, tzinfo=utc), verbose_name='Время закрытия смены'),
        ),
        migrations.AlterField(
            model_name='session',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 9, 21, 11, 469905, tzinfo=utc), verbose_name='Время открытия смены'),
        ),
    ]