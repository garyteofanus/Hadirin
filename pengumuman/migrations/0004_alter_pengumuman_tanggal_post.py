# Generated by Django 3.2.9 on 2021-12-07 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengumuman', '0003_alter_pengumuman_tanggal_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengumuman',
            name='tanggal_post',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]