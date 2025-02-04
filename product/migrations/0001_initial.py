# Generated by Django 5.1.4 on 2024-12-16 09:07

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Product Name')),
                ('is_warranty_active', models.BooleanField(default=True, help_text='Indicates if the product warranty is still valid.', verbose_name='Is Warranty Active')),
                ('warranty_period', models.IntegerField(help_text='Warranty duration in months.', verbose_name='Warranty Period (Months)')),
                ('sold_date', models.DateField(default=datetime.date.today, help_text='Date when the product was sold.', verbose_name='Date Sold')),
                ('serial_number', models.CharField(help_text='Unique identifier for the product.', max_length=100, unique=True, verbose_name='Serial Number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.client')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-created_at'],
            },
        ),
    ]
