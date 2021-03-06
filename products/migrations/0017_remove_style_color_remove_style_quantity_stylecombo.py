# Generated by Django 4.0.3 on 2022-05-03 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_colors_style_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='style',
            name='color',
        ),
        migrations.RemoveField(
            model_name='style',
            name='quantity',
        ),
        migrations.CreateModel(
            name='StyleCombo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity required')),
                ('color', models.ManyToManyField(to='products.colors')),
                ('style_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.style')),
            ],
        ),
    ]
