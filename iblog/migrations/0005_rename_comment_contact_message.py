# Generated by Django 3.2.13 on 2022-05-25 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iblog', '0004_contact_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='comment',
            new_name='message',
        ),
    ]
