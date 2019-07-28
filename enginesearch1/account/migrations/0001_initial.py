# Generated by Django 2.0.1 on 2018-08-26 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, db_index=True, max_length=150, null=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('url', models.CharField(default='www.exampleurl.com', max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('rating',),
            },
        ),
        migrations.CreateModel(
            name='Mixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stock', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.FileField(null=True, upload_to='products/mixture/')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('available', models.NullBooleanField(default=True)),
                ('stock', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('number', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='account.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100, null=True)),
                ('city', models.CharField(default='', max_length=100, null=True)),
                ('website', models.URLField(blank=True, default='', max_length=100, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='products/profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
        migrations.AlterIndexTogether(
            name='mixture',
            index_together={('id', 'slug')},
        ),
    ]