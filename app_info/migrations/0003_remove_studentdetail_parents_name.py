# Generated by Django 4.0.5 on 2022-07-13 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_info', '0002_studentdetail_parents_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetail',
            name='parents_name',
        ),
    ]
