# Generated by Django 3.2.13 on 2022-07-08 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_books', '0002_alter_accountdetail_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetail',
            name='account_type',
            field=models.CharField(choices=[('0', '지출'), ('1', '수입')], default='0', max_length=10),
        ),
    ]
