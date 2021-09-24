# Generated by Django 3.2.7 on 2021-09-24 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.CharField(max_length=155, null=True)),
                ('instagram', models.CharField(max_length=155, null=True)),
                ('tiktok', models.CharField(max_length=155, null=True)),
                ('youtube', models.CharField(max_length=155, null=True)),
                ('facebook', models.CharField(max_length=155, null=True)),
                ('mail', models.CharField(max_length=129, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, null=True)),
                ('kasb', models.CharField(max_length=100, null=True)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('job', models.CharField(max_length=120, null=True)),
                ('shior', models.CharField(max_length=125, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reja_teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reja', models.CharField(max_length=130, null=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='royalapp.teacher')),
            ],
        ),
    ]
