# Generated by Django 2.1.2 on 2019-03-05 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leituras', '0026_auto_20190305_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='serie',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='leituras.Serie'),
        ),
    ]
