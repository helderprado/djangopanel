# Generated by Django 3.0.5 on 2020-04-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0008_auto_20200405_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='observacoes',
            field=models.CharField(blank='', default='', max_length=100, null=''),
        ),
    ]
