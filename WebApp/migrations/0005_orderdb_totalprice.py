# Generated by Django 5.0.4 on 2024-06-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_orderdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdb',
            name='totalprice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]