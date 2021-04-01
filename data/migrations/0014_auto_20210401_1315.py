# Generated by Django 3.1.6 on 2021-04-01 10:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20210331_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='positionType',
        ),
        migrations.AddField(
            model_name='order',
            name='positionType',
            field=models.CharField(blank=True, choices=[('FG', 'Гостю'), ('FS', 'Себе'), ('B', 'Бонусный')], default='FG', max_length=2, verbose_name='Тип кальяна'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 1, 10, 15, 52, 328807, tzinfo=utc), verbose_name='Дата приёма на работу'),
        ),
        migrations.AlterField(
            model_name='session',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 10, 15, 52, 330800, tzinfo=utc), verbose_name='Время закрытия смены'),
        ),
        migrations.AlterField(
            model_name='session',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 10, 15, 52, 330800, tzinfo=utc), verbose_name='Время открытия смены'),
        ),
    ]
