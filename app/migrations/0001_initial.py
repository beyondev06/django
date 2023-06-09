# Generated by Django 2.1.5 on 2023-01-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('about', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('actual_price', models.FloatField(max_length=20)),
                ('sale_price', models.FloatField(max_length=100)),
                ('tax', models.FloatField(max_length=10)),
                ('tax_price', models.FloatField(max_length=10)),
                ('image_1', models.ImageField(default='', upload_to='images/')),
                ('image_2', models.ImageField(default='', upload_to='images/')),
                ('image_3', models.ImageField(default='', upload_to='images/')),
                ('category', models.CharField(max_length=10)),
                ('features', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=50)),
                ('expiry_date', models.DateField()),
                ('quantity', models.IntegerField(max_length=10000)),
                ('product_id', models.IntegerField(max_length=10000)),
                ('diettype', models.CharField(max_length=1000)),
                ('volume', models.CharField(max_length=1000)),
                ('weight', models.IntegerField(max_length=1000)),
                ('specification', models.TextField(max_length=1000)),
                ('minorder', models.CharField(max_length=1000)),
            ],
        ),
    ]
