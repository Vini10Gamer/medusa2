from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Profile, Turma


def is_user_escola(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return HttpResponseRedirect(reverse('login')+'?next='+request.path)
        profile, c = Profile.objects.get_or_create(user=request.user, defaults={'is_aluno': False, 'is_professor': False})
        if (profile.is_aluno
                or profile.is_aluno
                or request.user.is_staff
                or request.user.is_superuser):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_has_perm_or_turma_cargo(perm, lider=True, regente=True, cargo_geral=False, alter_qualquer=False):
    def decorator(function):
        def wrap(request, *args, **kwargs):
            if request.user.has_perm(perm):
                if alter_qualquer:
                    return function(request, qualquer=True, *args, **kwargs)
                else:
                    return function(request, *args, **kwargs)

            turma = Turma.objects.get(pk=kwargs['turma_pk'])

            if turma.is_lider(request.user) and lider:
                if alter_qualquer:
                    return function(request, qualquer=False, *args, **kwargs)
                else:
                    return function(request, *args, **kwargs)
            if turma.is_regente(request.user) and regente:
                if alter_qualquer:
                    return function(request, qualquer=False, *args, **kwargs)
                else:
                    return function(request, *args, **kwargs)
            if turma.is_user_especial(request.user) and cargo_geral:
                if alter_qualquer:
                    return function(request, qualquer=False, *args, **kwargs)
                else:
                    return function(request, *args, **kwargs)
            raise PermissionDenied

        wrap.__doc__ = function.__doc__
        wrap.__name__ = function.__name__
        return wrap

    return decorator
