# Generated by Django 4.1.6 on 2023-03-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mobile_Inspectionapp', '0004_remove_leadaddress_customer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('dispatcher', 'dispatcher'), ('customer', 'customer')], default='', max_length=50, null=True),
        ),
    ]
