# Generated by Django 4.0.3 on 2022-04-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_measurementchart_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='task_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='processes',
            name='task_status',
            field=models.BooleanField(default=False),
        ),
    ]
