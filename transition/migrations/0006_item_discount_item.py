# Generated by Django 4.1.6 on 2023-02-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transition', '0005_tax_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_item',
            field=models.BooleanField(default=True),
        ),
    ]
