# Generated by Django 5.0.6 on 2024-06-08 17:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_slug', models.SlugField(unique=True)),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField(default=0)),
                ('product_demo_price', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMetaInformation',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('product_quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('product_measuring', models.CharField(blank=True, choices=[('KG', 'KG'), ('ML', 'ML'), ('L', 'L')], max_length=100, null=True)),
                ('is_restrict', models.BooleanField(default=False)),
                ('restrict_quantity', models.IntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meta_info', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]