# Generated by Django 4.0.3 on 2022-04-12 11:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_group', models.CharField(max_length=20, verbose_name='Product group')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_no', models.CharField(max_length=20, unique=True)),
                ('style_description', models.TextField(max_length=100, verbose_name='Style description')),
                ('size', models.CharField(max_length=10)),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity required')),
                ('delivery_date', models.DateField(default=datetime.date.today, verbose_name='Delivery date')),
                ('product_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productgroup')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.season')),
            ],
        ),
        migrations.CreateModel(
            name='Processes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_name', models.CharField(max_length=50, verbose_name='Accessories name')),
                ('purchase_units', models.CharField(max_length=10, verbose_name='Purchase units')),
                ('qty_per_item', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Quantity per item')),
                ('style_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.style')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='suppliers.suppliers')),
            ],
        ),
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50, verbose_name='Accessories name')),
                ('purchase_units', models.CharField(max_length=10, verbose_name='Purchase units')),
                ('qty_per_item', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Quantity per item')),
                ('style_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.style')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='suppliers.suppliers')),
            ],
        ),
    ]
