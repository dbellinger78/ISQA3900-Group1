# Generated by Django 3.2.8 on 2021-11-17 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
    ]