# Generated by Django 5.0.4 on 2024-05-14 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_delete_cadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='agente',
            name='ativo',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='ativo',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
