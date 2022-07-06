# Generated by Django 3.2.13 on 2022-07-04 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('book_name', models.CharField(max_length=100)),
                ('budget', models.DecimalField(decimal_places=0, max_digits=9)),
                ('delete_flag', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_books', to='users.user', verbose_name='유저')),
            ],
            options={
                'db_table': 'account_books',
            },
        ),
        migrations.CreateModel(
            name='AccountCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'account_category',
            },
        ),
        migrations.CreateModel(
            name='AccountDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('written_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=9)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('account_type', models.CharField(max_length=10)),
                ('delete_flag', models.BooleanField(default=False)),
                ('account_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_books.accountbook', verbose_name='가계부')),
                ('account_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_books.accountcategory', verbose_name='카테고리')),
            ],
            options={
                'db_table': 'account_detail',
            },
        ),
    ]