# Generated by Django 4.2.3 on 2023-07-18 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Service',
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
    ]
