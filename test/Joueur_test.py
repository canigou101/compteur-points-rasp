import pytest
from src.model.Joueur import Joueur

# ==========================================
# TESTS UNITAIRES POUR LA CLASSE JOUEUR
# ==========================================

def test_initialisation_joueur():

    

    """Vérifie qu'un joueur est correctement créé avec son nom et prénom."""
    joueur = Joueur(N="Zidane", P="Zinédine")
    
    assert joueur.Nom == "Zidane"
    assert joueur.Prenom == "Zinédine"

