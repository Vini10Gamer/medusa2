# Generated by Django 2.1.8 on 2019-05-12 23:53

#  Developed by Vinicius José Fritzen
#  Last Modified 12/05/19 20:54.
#  Copyright (c) 2019  Vinicius José Fritzen and Albert Angel Lanzarini

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import escola.customFields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escola', '0026_auto_20190428_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaConhecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Area', to='escola.Turma')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('data', models.DateTimeField()),
                ('descricao', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='ItemAvaliativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=90)),
                ('numero', models.IntegerField()),
                ('nota', escola.customFields.JSONField(blank=True, null=True)),
                ('metodoNota', models.CharField(choices=[('CONCEITO', 'Conceito'), ('PORCENTAGEM', 'Porcentagem')], max_length=30)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='EventoTurma',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escola.Evento')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('escola.evento',),
        ),
        migrations.CreateModel(
            name='ItemAvaliativoArea',
            fields=[
                ('itemavaliativo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escola.ItemAvaliativo')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.AreaConhecimento')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('escola.itemavaliativo',),
        ),
        migrations.CreateModel(
            name='ItemAvaliativoMateria',
            fields=[
                ('itemavaliativo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escola.ItemAvaliativo')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('escola.itemavaliativo',),
        ),
        migrations.AddField(
            model_name='itemavaliativo',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_escola.itemavaliativo_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='evento',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evento',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_escola.evento_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='materiadaturma',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materias', to='escola.AreaConhecimento'),
        ),
        migrations.CreateModel(
            name='ProvaMarcada',
            fields=[
                ('eventoturma_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escola.EventoTurma')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('escola.eventoturma',),
        ),
        migrations.AddField(
            model_name='itemavaliativomateria',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.MateriaDaTurma'),
        ),
        migrations.AddField(
            model_name='eventoturma',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.Turma'),
        ),
        migrations.CreateModel(
            name='ProvaAreaMarcada',
            fields=[
                ('provamarcada_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escola.ProvaMarcada')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.AreaConhecimento')),
                ('item_avaliativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.ItemAvaliativoArea')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('escola.provamarcada',),
        ),
        migrations.CreateModel(
            name='ProvaMateriaMarcada',
            fields=[
                ('provamarcada_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escola.ProvaMarcada')),
                ('item_avaliativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.ItemAvaliativoMateria')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.MateriaDaTurma')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('escola.provamarcada',),
        ),
        migrations.AddField(
            model_name='provamarcada',
            name='conteudo',
            field=models.ManyToManyField(to='escola.Conteudo'),
        ),
    ]
