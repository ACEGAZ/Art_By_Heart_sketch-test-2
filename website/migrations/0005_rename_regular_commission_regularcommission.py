# Generated by Django 3.2.14 on 2022-09-16 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rename_reference_sheet_commission_referencesheetcommission'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='regular_commission',
            new_name='RegularCommission',
        ),
    ]
