# Generated by Django 2.0.6 on 2018-06-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userscalendar', '0007_auto_20180624_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='month',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]