# Generated by Django 3.1.7 on 2021-03-10 11:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20210310_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 10, 11, 52, 14, 878668, tzinfo=utc), verbose_name='Дата приёма на работу'),
        ),
        migrations.AlterField(
            model_name='session',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 11, 52, 14, 881391, tzinfo=utc), verbose_name='Время закрытия смены'),
        ),
        migrations.AlterField(
            model_name='session',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 11, 52, 14, 881351, tzinfo=utc), verbose_name='Время открытия смены'),
        ),
    ]
