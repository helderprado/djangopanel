# Generated by Django 3.0.5 on 2020-04-05 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_order_observaçoes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='observaçoes',
            new_name='observacoes',
        ),
    ]
