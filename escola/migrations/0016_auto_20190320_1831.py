# Generated by Django 2.1.7 on 2019-03-20 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0015_auto_20190318_1640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horario',
            options={'permissions': (('editar_horario', 'Pode Editar o horario de qualquer turma.'),)},
        ),
    ]
