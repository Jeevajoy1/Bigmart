# Generated by Django 5.0.4 on 2024-05-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=100, null=True)),
                ('pname', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.TextField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('pimage', models.ImageField(blank=True, null=True, upload_to='Product Images')),
            ],
        ),
    ]
