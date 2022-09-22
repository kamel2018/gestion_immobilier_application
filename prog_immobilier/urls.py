"""Model urls.py pour specifier chaque endpoint le user va entrer
pour le requesting"""
from django.urls import path
from .views import (
    appartement_prix,
    get_appartements_api,
    save_appartement,
    creer_appartement,
    list_appartement,
    appartement_prix,
    programme_piscine,
    prog_promo_code,
)


urlpatterns = [
    path("", get_appartements_api, name="appartements"),
    path("insert_appartmenet_api/", save_appartement, name="save_appart_data"),
    path(
        "creer_appartement/<str:f_k>/", creer_appartement, name="creation_appartement"
    ),
    path("list_appartement_active/", list_appartement, name="list_appart_active"),
    path("list_appartement_prix/", appartement_prix, name="list_appart_prix"),
    path("list_prog_piscine/", programme_piscine, name="list_prog_piscine"),
    path("promo_code_appart/<str:promo_code>", prog_promo_code, name="promo_appart"),
]
