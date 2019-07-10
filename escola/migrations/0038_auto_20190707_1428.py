# Generated by Django 2.2.2 on 2019-07-07 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escola', '0037_profile_receber_email_notificacao'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SeguidorManager',
            new_name='Notificador',
        ),
        migrations.RenameField(
            model_name='tarefa',
            old_name='manager_seguidor',
            new_name='noti_comentario',
        ),
        migrations.AddField(
            model_name='turma',
            name='noti_aviso_geral_professor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='escola.Notificador'),
        ),
        migrations.AddField(
            model_name='turma',
            name='noti_nova_prova',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='escola.Notificador'),
        ),
        migrations.AddField(
            model_name='turma',
            name='noti_nova_tarefa',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='escola.Notificador'),
        ),
        migrations.AddField(
            model_name='turma',
            name='noti_novo_conteudo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='escola.Notificador'),
        ),
        migrations.AddField(
            model_name='turma',
            name='noti_prova_proxima',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='escola.Notificador'),
        ),
        migrations.AddField(
            model_name='turma',
            name='noti_tarefa_completa_proxima',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='escola.Notificador'),
        ),
        migrations.AddField(
            model_name='turma',
            name='noti_tarefa_nao_completa_proxima',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='escola.Notificador'),
        ),
    ]