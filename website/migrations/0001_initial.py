# Generated by Django 3.2.14 on 2022-09-13 10:01

import cloudinary.models
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
            name='add_art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='custom_commissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100)),
                ('colours', models.CharField(max_length=100)),
                ('traits', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('accessories', models.CharField(max_length=100)),
                ('other_info', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='reference_sheet_commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_reference', models.CharField(max_length=100)),
                ('character_owner', models.CharField(max_length=100)),
                ('design_changes', models.CharField(max_length=100)),
                ('add_ons', models.CharField(max_length=100)),
                ('other_info', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='regular_commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_reference', models.CharField(max_length=100)),
                ('character_owner', models.CharField(max_length=100)),
                ('commission_type', models.CharField(max_length=100)),
                ('type_option', models.CharField(max_length=100)),
                ('character_personality', models.CharField(max_length=100)),
                ('pose', models.CharField(max_length=100)),
                ('other_info', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='whatever',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.add_art')),
            ],
        ),
    ]
