# Generated by Django 3.1.3 on 2022-04-25 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220425_0439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice',
            new_name='choice_text',
        ),
    ]
