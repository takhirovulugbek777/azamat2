# Generated by Django 5.1.4 on 2024-12-17 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='product.client'),
        ),
    ]
