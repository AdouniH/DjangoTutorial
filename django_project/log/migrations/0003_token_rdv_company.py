# Generated by Django 2.2.4 on 2019-09-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20190903_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='token_rdv',
            name='company',
            field=models.EmailField(default='toto', max_length=254, verbose_name="Nom de l'entreprise"),
            preserve_default=False,
        ),
    ]
