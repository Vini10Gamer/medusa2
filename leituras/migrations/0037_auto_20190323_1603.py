# Generated by Django 2.1.7 on 2019-03-23 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leituras', '0036_auto_20190323_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='serie',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='leituras.Serie'),
        ),
    ]