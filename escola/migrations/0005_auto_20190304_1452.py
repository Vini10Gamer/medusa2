# Generated by Django 2.1.2 on 2019-03-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_cargoturma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='is_lider',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='chamada',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]