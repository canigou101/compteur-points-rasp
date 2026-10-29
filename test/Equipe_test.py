import pytest
from src.model.Equipe import Equipe
from src.model.Joueur import Joueur
# ==========================================
# TESTS UNITAIRES POUR LA CLASSE EQUIPE
# ==========================================

def test_initialisation_equipe():
    """Vérifie qu'une équipe est créée avec le bon nom et une liste vide de joueurs."""
    equipe = Equipe(S="Real Madrid")
    
    assert equipe.NomEquipe == "Real Madrid"
    assert isinstance(equipe.Joueurs, list)
    assert len(equipe.Joueurs) == 0


def test_ajout_un_joueur():
    """Vérifie l'ajout réussi d'un joueur dans l'équipe."""
    equipe = Equipe(S="Paris SG")
    joueur = Joueur(N="Mbappé", P="Kylian")
    
    equipe.ajoutJoueur(joueur)
    
    assert len(equipe.Joueurs) == 1
    assert equipe.Joueurs[0] == joueur
    assert equipe.Joueurs[0].Nom == "Mbappé"


def test_ajout_plusieurs_joueurs():
    """Vérifie l'ajout de plusieurs joueurs consécutifs."""
    equipe = Equipe(S="Équipe de France")
    j1 = Joueur(N="Griezmann", P="Antoine")
    j2 = Joueur(N="Giroud", P="Olivier")
    
    equipe.ajoutJoueur(j1)
    equipe.ajoutJoueur(j2)
    
    assert len(equipe.Joueurs) == 2
    assert j1 in equipe.Joueurs
    assert j2 in equipe.Joueurs