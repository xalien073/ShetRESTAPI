# Generated by Django 3.0.5 on 2021-05-23 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=12)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('old_price', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='shop/images')),
                ('slug', models.CharField(blank=True, max_length=1000, unique=True)),
                ('Ratings', models.CharField(blank=True, default=0, max_length=500)),
                ('Total_Reviews', models.PositiveIntegerField(blank=True, default=0)),
                ('In_Stock', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Store.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='E_Store.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Searche',
            fields=[
                ('search_number', models.AutoField(primary_key=True, serialize=False)),
                ('searches', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='StarRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True)),
                ('stars', models.IntegerField(blank=True, null=True)),
                ('timeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='E_Store.Product')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
