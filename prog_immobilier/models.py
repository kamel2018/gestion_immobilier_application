"""La structuration de la base des donnees 
via la creation des tableaux par la definition en class"""
from django.db import models
from multiselectfield import MultiSelectField


class Programme_immobilier(models.Model):
    """Definition d'un Database-Table
    pour sauvegarder les donnees des programmes immobilier"""

    nom_prog = models.CharField(
        primary_key=True, max_length=100, blank=False, unique=True
    )
    is_active = models.BooleanField()

    def __str__(self) -> str:
        """Retourn chaque nom du programme"""
        return f"{self.nom_prog}"


class Appartement(models.Model):
    """Definition d'un Database-Table pour sauvegarder les donnees d'appartements
    pour chaque programme_immobilier
    La clé primaire sera générée automatiquement comme id pour chaque Appartement"""

    Proche_station_ski = "Proche station ski"
    Piscine = "Piscine"
    Jardin = "Jardin"
    Cave = "Cave"
    Parking = "Parking"

    choix = (
        (Proche_station_ski, "Proche station ski"),
        (Piscine, "Piscine"),
        (Jardin, "Jardin"),
        (Cave, "Cave"),
        (Parking, "Parking"),
    )

    surface = models.FloatField()
    prix = models.FloatField()
    nombre_piece = models.IntegerField()

    list_caracteristiques = MultiSelectField(choices=choix, max_length=200)
    program = models.ForeignKey(Programme_immobilier, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Retourne le nombre d'appartement
        pour chaque nom du programme immobilier"""
        return f"Appartement {self.id} de {self.program_id}"
