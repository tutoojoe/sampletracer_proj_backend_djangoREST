# Generated by Django 4.0.3 on 2022-04-23 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0004_customermore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Email address of user for registration and login purposes', max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('NEWUSER', 'NewUser'), ('MANAGER', 'Manager'), ('CUSTOMER', 'Customer'), ('JUNIOREMP', 'JuniorEmp'), ('STOREKEEPER', 'Storekeeper')], default='NEWUSER', help_text='User type/role - to be selected from the given list. This will determine the permissions. \nDefault value will be NEWUSER on registration.', max_length=50, verbose_name='Type of user'),
        ),
    ]