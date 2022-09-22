"""Function based views, Creations des views basé sur des fonctions pour le chargement des donnees 
de programmes d'immobilier et appartements, la creation des APIs des d'appartement"""
import requests
from django.db.models import Q, F
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Programme_immobilier, Appartement
from .serializers import AppartementSerializer


@api_view(["GET"])
def get_appartements_api(request) -> str:
    """Creation d'api appartement pour envoyé les donnees via le chemin (endpoint)"""
    if request:
        appartements = Appartement.objects.all()
        serializer = AppartementSerializer(appartements, many=True)
        appart_data = serializer.data
        return render(request, "prog_immobilier/index.html", {"data": appart_data})


@api_view(["POST"])
def save_appartement(request):
    """Fonction pour le sauvegarde des donnees appartements entrées par l'utilisateur"""
    if request.method == "POST":
        save_serializer = AppartementSerializerForSaving(data=request.data)
        if save_serializer.is_valid():
            save_serializer.save()
        return Response(save_serializer.data, status=status.HTTP_201_CREATED)


def creer_appartement(request: str, f_k: str):
    """La creation d'appartement via les donnees reçu du code HTML(inputs)
    et les envoyer à travers le chemin(endpoint) appartement"""
    if request.method == "POST":
        surface = request.POST.get("surface")
        prix = request.POST.get("prix")
        nombre_piece = request.POST.get("nombre_piece")

        temp_list = []

        if request.POST.get("Proche station ski"):
            temp_list.append(request.POST.get("Proche station ski"))
        if request.POST.get("Piscine"):
            temp_list.append(request.POST.get("Piscine"))
        if request.POST.get("Jardin"):
            temp_list.append(request.POST.get("Jardin"))
        if request.POST.get("Cave"):
            temp_list.append(request.POST.get("Cave"))
        if request.POST.get("Parking"):
            temp_list.append(request.POST.get("Parking"))

        list_caracteristiques = temp_list
        program = f_k
        data = {
            "surface": surface,
            "prix": prix,
            "nombre_piece": nombre_piece,
            "list_caracteristiques": list_caracteristiques,
            "program": program,
        }
        print(list_caracteristiques)
        headers = {"Content-Type": "application/json"}
        requests.post(
            "http://127.0.0.1:8000/insert_appartmenet_api/", json=data, headers=headers
        )
        return render(request, "prog_immobilier/creation_appartement.html")
    else:
        return render(request, "prog_immobilier/creation_appartement.html")


def list_appartement(request) -> str:
    """Querysets pour lister tous les appartement ayant des programmes immobilier actifs"""
    appart_active_prog = Appartement.objects.filter(program__is_active=True)
    return render(
        request,
        "prog_immobilier/querysets.html",
        {"appart_active_prog": appart_active_prog},
    )


def appartement_prix(request) -> str:
    """Querysets  pour lister tous les appartements ayant un prix dans l'interval[100-180]"""
    appart_prix_range = Appartement.objects.filter(Q(prix__gte=100) & Q(prix__lte=180))
    print(appart_prix_range)
    return render(
        request,
        "prog_immobilier/querysets1.html",
        {"appart_prix_range": appart_prix_range},
    )


def programme_piscine(request) -> str:
    """Querysets pour lister tous les programmes immobilier ayant au moins (Piscine) comme caracteristique"""
    progs_avec_piscine = Programme_immobilier.objects.filter(
        appartement__list_caracteristiques__contains="Piscine"
    )
    return render(
        request,
        "prog_immobilier/querysets2.html",
        {"progs_avec_piscine": progs_avec_piscine},
    )


def prog_promo_code(request: str, promo_code: str):
    """Querysets pour reduire le prix en le faire baisser de 5% pour tous
    les appartements si le promo code (PERE NOEL) est passé comme argument
    et en changeant label du programme en PROMO SPECIALE"""
    if request:
        if promo_code == "PERE NOEL":
            promo_code_queryset = Appartement.objects.annotate(
                reduction_prix=F("prix") / 100 - 0.05, PROMO_SPECIALE=F("program")
            )
    return render(
        request,
        "prog_immobilier/querysets3.html",
        {"promo_code_queryset": promo_code_queryset},
    )


# def appartement_saison(request, saison):
"""J'ai compris la logique de la fonction, que à chaque data entrée en argument,
Querysets va lister les appartements selon la saison et les faire trier à chaque fois par un caracteristique, prix
et la surface, mais je l'ai mis en commentaire, car il ya des bugs"""
#     year = str(date.year)
#     saisons = {'spring': pd.date_range(start='21/03/'+year, end='20/06/'+year),
#                'summer': pd.date_range(start='21/06/'+year, end='22/09/'+year),
#                'automne': pd.date_range(start='23/09/'+year, end='20/12/'+year),
#                'winter': pd.date_range(start='21/12/'+year, end='20/03/'+year),}

#     if saison in saisons['winter']:
#         querysets =
#     if saison in saisons['summer']:
#         querysets =
#     if saison in saisons['automne']:
#         querysets =
#     if saison in saisons['spring']:
#         querysets =

#     return render(request, '.html', {'data':data})
