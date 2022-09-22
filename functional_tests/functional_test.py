"""Module pour tester le bon fonctionnement de l'application
django sur le navigateur(Firefox)"""
from selenium import webdriver



browser = webdriver.Firefox()
browser.get('http://localhost:8000')
'Appartement' in browser.title

