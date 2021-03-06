# Generated by Django 4.0.3 on 2022-06-02 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0021_remove_comments_style_remove_measurements_mc_name_and_more'),
        ('suppliers', '0002_suppliers_created_at_suppliers_last_update_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50, verbose_name='Accessories name')),
                ('purchase_units', models.CharField(max_length=10, verbose_name='Purchase units')),
                ('qty_per_item', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Quantity per item')),
                ('task_status', models.BooleanField(default=False)),
                ('target_date', models.DateField(blank=True, null=True)),
                ('finish_date', models.DateField(blank=True, null=True)),
                ('assigned_by', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ManyToManyField(blank=True, null=True, related_name='accessory_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('style_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessories', to='products.style')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='suppliers.suppliers')),
            ],
            options={
                'verbose_name': 'Accessory',
                'verbose_name_plural': 'Accessories',
                'ordering': ['item_name'],
            },
        ),
    ]
