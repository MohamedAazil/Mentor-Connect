# Generated by Django 5.0.7 on 2024-08-04 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='entrepreneur',
            new_name='email',
        ),
    ]
