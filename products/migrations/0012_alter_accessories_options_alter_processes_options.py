# Generated by Django 4.0.3 on 2022-04-27 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_style_edited_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessories',
            options={'ordering': ['item_name'], 'verbose_name': 'Accessory', 'verbose_name_plural': 'Accessories'},
        ),
        migrations.AlterModelOptions(
            name='processes',
            options={'ordering': ['process_name'], 'verbose_name': 'Process', 'verbose_name_plural': 'Processes'},
        ),
    ]
