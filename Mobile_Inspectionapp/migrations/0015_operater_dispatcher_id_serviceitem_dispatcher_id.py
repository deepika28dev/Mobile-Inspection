# Generated by Django 4.1.6 on 2023-03-23 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mobile_Inspectionapp', '0014_user_dispatcher_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='operater',
            name='dispatcher_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='serviceitem',
            name='dispatcher_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
