# Generated by Django 5.2.3 on 2025-06-25 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0007_remove_matricula_costo_delete_costo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('matricula', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='costo_asociado', to='administrativo.matricula')),
            ],
        ),
        migrations.AddField(
            model_name='matricula',
            name='costo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matricula_asociada', to='administrativo.costo'),
        ),
    ]
