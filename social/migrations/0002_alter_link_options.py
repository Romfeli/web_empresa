# Generated by Django 4.2.3 on 2023-07-21 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-created'], 'verbose_name': 'enlace', 'verbose_name_plural': 'enlaces'},
        ),
    ]
