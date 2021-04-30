# Generated by Django 3.1.6 on 2021-04-27 20:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20210426_1041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addtosession',
            options={'verbose_name': 'Привоз', 'verbose_name_plural': 'Привозы'},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='fathName',
            new_name='thirdName',
        ),
        migrations.RemoveField(
            model_name='place',
            name='percentForPlace',
        ),
        migrations.RemoveField(
            model_name='place',
            name='percentForWorker',
        ),
        migrations.RemoveField(
            model_name='position',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='famName',
        ),
        migrations.AddField(
            model_name='profile',
            name='secondName',
            field=models.CharField(default='Фамилия', max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 27, 20, 40, 38, 555450, tzinfo=utc), verbose_name='Дата приёма на работу'),
        ),
        migrations.AlterField(
            model_name='session',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 20, 40, 38, 557444, tzinfo=utc), verbose_name='Время закрытия смены'),
        ),
        migrations.AlterField(
            model_name='session',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 20, 40, 38, 557444, tzinfo=utc), verbose_name='Время открытия смены'),
        ),
        migrations.CreateModel(
            name='Percents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField(verbose_name='Стоимость')),
                ('percentForWorker', models.FloatField(verbose_name='Процент работника')),
                ('percentForLid', models.FloatField(verbose_name='Доход от позиции')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.place', verbose_name='Заведение')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.position', verbose_name='Позиция')),
            ],
        ),
    ]