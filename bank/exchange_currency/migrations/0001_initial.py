# Generated by Django 4.2.5 on 2023-09-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_code', models.CharField(max_length=3, unique=True)),
                ('rate', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
    ]
