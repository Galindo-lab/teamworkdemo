from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator

import json


class Profile(models.Model):
    """
    Esta clase permite agregar informacion adicional de los usuarios
    permite extender los perfiles sin modificar User
    """

    # TODO: agregar un campo que represente el perfil global 

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    


class Group(models.Model):
    """
    Modelo para representar un grupo al que se puede integrar un miembro
    """
    name = models.CharField(
        max_length=200
    )

    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_admin'
    )

    class Meta:
        # permite que haya nombre repetidos mientras el administrador
        # no sea el mismo

        unique_together = (
            ('name', 'admin'),
        )


class Member(models.Model):
    """
    Relaciona los miembros con los grupos 
    """

    member = models.ForeignKey(
        User,
        related_name='group_member',
        on_delete=models.CASCADE
    )

    group = models.ForeignKey(
        Group,
        related_name='members',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (
            ('member', 'group'),
        )


class BelbinUserProfile(models.Model):
    """
    formularios realizados
    """

    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )

    timestamp = models.DateTimeField(
        default=timezone.now
    )

    # perfiles de belbin
    resource_investigator = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    team_worker = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    coordinator = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    plant = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    monitor_evaluator = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    specialist = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    shaper = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    implementer = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    completer_finisher = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    def json_profiles(self):

        diccionario = {
            "resource_investigator": self.resource_investigator,
            "team_worker": self.team_worker,
            "coordinator": self.coordinator,
            "plant": self.plant,
            "monitor_evaluator": self.monitor_evaluator,
            "specialist": self.specialist,
            "shaper": self.shaper,
            "implementer": self.implementer,
            "completer_finisher": self.completer_finisher,
        }

        return json.dumps(diccionario)

    class Meta:
        ordering = ['-timestamp']
