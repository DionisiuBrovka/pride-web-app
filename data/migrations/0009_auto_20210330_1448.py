# Generated by Django 3.1.6 on 2021-03-30 11:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20210330_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='activate',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 30, 11, 48, 36, 580895, tzinfo=utc), verbose_name='Дата приёма на работу'),
        ),
        migrations.AlterField(
            model_name='session',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 11, 48, 36, 582854, tzinfo=utc), verbose_name='Время закрытия смены'),
        ),
        migrations.AlterField(
            model_name='session',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 11, 48, 36, 582854, tzinfo=utc), verbose_name='Время открытия смены'),
        ),
    ]