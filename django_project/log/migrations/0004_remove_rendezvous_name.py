# Generated by Django 2.2.4 on 2019-09-03 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20190903_0544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rendezvous',
            name='name',
        ),
    ]
