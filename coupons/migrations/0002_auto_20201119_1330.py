# Generated by Django 3.1.3 on 2020-11-19 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='valid_from',
            new_name='valid_form',
        ),
    ]
