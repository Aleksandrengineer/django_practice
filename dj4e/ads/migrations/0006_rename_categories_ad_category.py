# Generated by Django 3.2.4 on 2021-07-25 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_alter_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='categories',
            new_name='category',
        ),
    ]
