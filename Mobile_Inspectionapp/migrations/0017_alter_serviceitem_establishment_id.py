# Generated by Django 4.1.6 on 2023-03-23 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mobile_Inspectionapp', '0016_alter_serviceitem_establishment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceitem',
            name='establishment_id',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, to='Mobile_Inspectionapp.establishment'),
        ),
    ]
