# Generated by Django 5.0.4 on 2024-05-14 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_remove_agente_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisor',
            name='usuario',
        ),
    ]
