# Generated by Django 5.0.4 on 2024-05-31 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_registerdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(blank=True, max_length=100, null=True)),
                ('productname', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('totalprice', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
