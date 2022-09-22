"""Creation des fixtures pour l'envoyer en argument
lors de testing """
import pytest


@pytest.fixture
def appartement_data():
    return {
        "surface": 20.0,
        "prix": 150.0,
        "nombre_piece": 4,
        "list_caracteristiques": [
            "Jardin",
            "Piscine",
            "Proche station ski",
            "Parking",
            "Cave",
        ],
    }
