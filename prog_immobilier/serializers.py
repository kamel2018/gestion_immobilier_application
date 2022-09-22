"""Module pour serialiser les donnees model 
et le convertir en type data (json)"""
from rest_framework import serializers, fields
from .models import Programme_immobilier, Appartement


class ProgramSerializer(serializers.ModelSerializer):
    """Serialisation des attibus des programmes immobilier"""

    class Meta:
        model = Programme_immobilier
        fields = "__all__"


choix = (
    ("Proche station ski", "Proche station ski"),
    ("Piscine", "Piscine"),
    ("Jardin", "Jardin"),
    ("Cave", "Cave"),
    ("Parking", "Parking"),
)


class CustomMultipleChoiceField(fields.MultipleChoiceField):
    """Les donnees pour les caracteristiques que l'utilisateur choisi"""

    def to_representation(self, value) -> str:
        """Representation des choix de la liste des caracteristiques
        d'appartement en type list pour faciliter l'accees au donnees
        lors des Querysets"""
        return list(super().to_representation(value))


class AppartementSerializer(serializers.ModelSerializer):
    """Serialisation des attibus des appartements"""

    list_caracteristiques = CustomMultipleChoiceField(choices=choix, required=True)

    class Meta:
        model = Appartement
        fields = ("surface", "prix", "nombre_piece", "list_caracteristiques", "program")
