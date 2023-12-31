# Generated by Django 4.2.5 on 2023-09-25 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0006_alter_contactus_date_alter_tutor_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='ach',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='sub',
            field=models.TextField(default='Math, Phy, Computer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2023, 9, 25, 21, 7, 59, 220712)),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2023, 9, 25, 21, 7, 59, 267583)),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='pic',
            field=models.ImageField(default='images/profile.jpg', upload_to='images/'),
        ),
    ]
