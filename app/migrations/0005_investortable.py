# Generated by Django 4.1.7 on 2023-04-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cart_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investortable',
            fields=[
                ('invid', models.AutoField(primary_key=True, serialize=False)),
                ('inv_name', models.CharField(max_length=100)),
                ('inv_phone', models.CharField(max_length=100)),
                ('inv_address', models.CharField(max_length=100)),
                ('inv_email', models.CharField(max_length=100)),
                ('inv_pass', models.CharField(max_length=100)),
                ('inv_loca', models.CharField(max_length=100)),
                ('inv1', models.CharField(default='', max_length=100)),
                ('inv2', models.CharField(default='', max_length=100)),
                ('inv3', models.CharField(default='', max_length=100)),
                ('inv4', models.CharField(default='', max_length=100)),
                ('inv5', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
