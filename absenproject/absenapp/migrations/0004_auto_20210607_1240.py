# Generated by Django 3.2.4 on 2021-06-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absenapp', '0003_absen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absen',
            name='absen_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='absen',
            name='absen_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]