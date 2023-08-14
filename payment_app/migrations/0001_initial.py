# Generated by Django 4.1.6 on 2023-03-15 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Mobile_Inspectionapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='capture_paypal_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=90, null=True)),
                ('capture_url', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Paypal Capture Payments',
            },
        ),
        migrations.CreateModel(
            name='paypal_token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paypal_access_token', models.CharField(max_length=900)),
            ],
        ),
        migrations.CreateModel(
            name='stripe_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('receipt_id', models.CharField(max_length=90)),
                ('user_id', models.CharField(max_length=90)),
                ('checkout_id', models.CharField(max_length=90)),
                ('amount_received', models.CharField(max_length=90)),
                ('payment_intent_id', models.CharField(max_length=90)),
                ('billing_details', models.TextField(blank=True, max_length=350, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('receipt_url', models.CharField(blank=True, max_length=90, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=250)),
                ('total_price', models.FloatField(default=0.0)),
                ('discount', models.CharField(max_length=250)),
                ('subtotal', models.FloatField(default=0.0)),
                ('payment_type', models.CharField(max_length=90)),
                ('status', models.CharField(default='pending', max_length=250)),
                ('establishment_data', models.CharField(max_length=250)),
                ('address_data', models.CharField(max_length=250)),
                ('contact_data', models.CharField(max_length=250)),
                ('First_name', models.CharField(max_length=250)),
                ('Last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=50)),
                ('street_number', models.CharField(max_length=250)),
                ('unit_number', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('address_1', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('zip_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mobile_Inspectionapp.service')),
                ('service_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mobile_Inspectionapp.servicetype')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Order',
            },
        ),
    ]
