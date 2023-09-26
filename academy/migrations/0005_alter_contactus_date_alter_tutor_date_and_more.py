# Generated by Django 4.2.5 on 2023-09-25 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0004_tutor_about_alter_contactus_date_alter_tutor_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2023, 9, 25, 17, 27, 19, 216323)),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2023, 9, 25, 17, 27, 19, 263213)),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
