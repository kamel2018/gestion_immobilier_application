"""Remplissage des tableau Programme_immobilier et Appartement
en utilisant Faker comme des donnees fake pour pouvoir
terster les Querysets a travers creation de la commande management"""

import random
from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from prog_immobilier.models import Programme_immobilier, Appartement

caracteristiques = [
    "Proche station ski",
    "Piscine",
    "Jardin",
    "Cave",
    "Parking",
]


class Provider(faker.providers.BaseProvider):
    """Produire les donnees fake"""

    def caracteristique_appart(self):
        """Indiquatin des donnees de la liste
        des caracteristiques pour le remplissage alreatoire
        des appartements"""
        return self.random_element(caracteristiques)


class Command(BaseCommand):
    """Creation de la commande management
    executée par python manage.py "commande" """

    help = "Command information"

    def handle(self, *args, **kwargs):
        """Le remplissage des donnees à
        travers la fonction handle
        lors de l'execution de la commande
        python manage.py jeu_donnees_aleatoires"""
        fake = Faker(["fr_FR"])
        fake.add_provider(Provider)

        for _ in range(10):
            """for loop pour les 10 programmes immobilier"""
            unique_val = fake.unique.company()
            bool_val = fake.boolean(chance_of_getting_true=10)
            Programme_immobilier.objects.create(nom_prog=unique_val, is_active=bool_val)

            for __ in range(20):
                """for loop pour les 20 appartement pour chaque programme
                dans les 10 programmes creé déja dans la boucle exterieur"""
                surf_app = round(random.uniform(20.00, 50.00), 2)
                prix_app = round(random.uniform(80.00, 300.00), 2)
                nombre_piece = random.randint(1, 20)
                carac1 = fake.caracteristique_appart()
                carac2 = fake.caracteristique_appart()
                prog_pk = unique_val

                while carac1 == carac2:
                    carac2 = fake.caracteristique_appart()
                list_carac_app = (carac1, carac2)
                Appartement.objects.create(
                    surface=surf_app,
                    prix=prix_app,
                    nombre_piece=nombre_piece,
                    list_caracteristiques=list_carac_app,
                    program_id=prog_pk,
                )

        check_programme = Programme_immobilier.objects.all().count()
        check_appartement = Appartement.objects.all().count()
        self.stdout.write(
            self.style.SUCCESS(
                f"{check_programme} Programmes d'immobilier sont ajoutés !"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"{check_appartement} Appartement d'immobilier sont ajoutés avec 2 caractèristiques pour chacune !"
            )
        )
