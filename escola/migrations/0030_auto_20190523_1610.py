# Generated by Django 2.1.8 on 2019-05-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0029_auto_20190523_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provamarcada',
            name='conteudos',
            field=models.ManyToManyField(blank=True, to='escola.Conteudo'),
        ),
    ]