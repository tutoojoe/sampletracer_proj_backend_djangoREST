# Generated by Django 4.0.3 on 2022-06-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_group', models.CharField(max_length=20, verbose_name='Product group')),
            ],
        ),
    ]
