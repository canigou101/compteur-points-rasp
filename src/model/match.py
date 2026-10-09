from .joueur import joueur
from .equipe import equipe
from .sport import sport

class match:
    """
   equipe du sport 

    """

    equipes : list[equipe]
    """les equipes qui joue le match"""
    Sport : sport
    """sport joué"""