# Generated by Django 2.2.1 on 2019-05-15 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190515_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='data_evento',
            new_name='data',
        ),
        migrations.AlterField(
            model_name='evento',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.Endereco'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='presenca',
            field=models.ManyToManyField(to='presenca.Presenca'),
        ),
    ]