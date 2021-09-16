# Generated by Django 3.2.7 on 2021-09-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=120, null=True)),
                ('email', models.EmailField(max_length=120, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(null=True, upload_to='employee-image')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]