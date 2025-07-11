# Generated by Django 5.2.3 on 2025-06-25 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0005_auto_20210610_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre de estudiante'),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='nombre',
            field=models.CharField(choices=[('1', 'Primero'), ('2', 'Segundo'), ('3', 'Tercero'), ('4', 'Cuarto'), ('5', 'Quinto'), ('6', 'Sexto')], max_length=30),
        ),
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
