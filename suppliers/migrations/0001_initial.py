# Generated by Django 4.0.3 on 2022-04-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=50)),
                ('supplier_email', models.EmailField(max_length=200)),
                ('supplier_phone', models.CharField(max_length=15)),
                ('supplier_address', models.TextField(max_length=255)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
    ]
