# Generated by Django 4.1.6 on 2023-03-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mobile_Inspectionapp', '0011_operater'),
    ]

    operations = [
        migrations.AddField(
            model_name='operater',
            name='operater_type',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
