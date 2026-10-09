from .joueur import joueur

class equipe:
    """
   equipe du sport 

    """

    nom : str
    """nom de l'equipe"""
    joueurs : list[joueur]
    """joueur dans l'équipe"""