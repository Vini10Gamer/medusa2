# Generated by Django 2.1.8 on 2019-04-26 02:13

#  Developed by Vinicius José Fritzen
#  Last Modified 25/04/19 23:18.
#  Copyright (c) 2019  Vinicius José Fritzen and Albert Angel Lanzarini

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0024_auto_20190425_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiadaturma',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materias', to='escola.Turma'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='materia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='escola.MateriaDaTurma'),
            preserve_default=False,
        ),
    ]
