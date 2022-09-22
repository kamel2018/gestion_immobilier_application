"""Tester tous les function views pour
l'automation et le bon fonctionnement
"""
from django.urls import reverse
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize(
    "param",
    [
        ("appartements"),
        ("list_appart_active"),
        ("list_appart_prix"),
        ("list_prog_piscine"),
    ],
)
def test_render_views(client, param) -> str:
    """Tester l'api d'appartements"""
    temp_url = reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_promo_code_appartement(client):
    """Tester les Querysets pour lister les appartement ayant PERE NOEL
    comme argument"""
    url = reverse("promo_appart", kwargs={"promo_code": "PERE NOEL"})
    resp = client.get(url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_creation_appartement(client, appartement_data):
    """Tester la creation d'appartement en utilisant
    le fixture appartement_data"""
    form_url = reverse("creation_appartement", kwargs={"f_k": "Blondel"})
    resp = client.post(form_url, data=appartement_data)
    assert resp.status_code == 200


pytest.mark.django_db
"""Tester l'insetion des donnees appartement via l'api rest de'appartement"""


def test_appartement_insertion_api(client, appartement_data):
    rest_form_url = reverse("save_appart_data")
    resp = client.post(rest_form_url, data=appartement_data)
    assert resp.status_code == 201
