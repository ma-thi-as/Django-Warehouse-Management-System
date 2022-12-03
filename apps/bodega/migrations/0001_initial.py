# Generated by Django 4.1.2 on 2022-11-19 13:27

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalInventario',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('opcion', models.CharField(choices=[('ENTRADAS', 'Entradas'), ('SALIDAS', 'Salidas')], max_length=10, verbose_name='Opcion')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad de productos')),
                ('salidas', models.IntegerField(blank=True, default=0, null=True, verbose_name='Salidas')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Inventario de producto',
                'verbose_name_plural': 'historical Inventario de productos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opcion', models.CharField(choices=[('ENTRADAS', 'Entradas'), ('SALIDAS', 'Salidas')], max_length=10, verbose_name='Opcion')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad de productos')),
                ('salidas', models.IntegerField(blank=True, default=0, null=True, verbose_name='Salidas')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Inventario de producto',
                'verbose_name_plural': 'Inventario de productos',
            },
        ),
    ]