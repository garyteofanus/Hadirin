# Generated by Django 3.2.9 on 2021-12-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presensi',
            name='keluar',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Keluar'),
        ),
    ]
