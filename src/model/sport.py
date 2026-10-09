from abc import ABC, abstractmethod




class sport(ABC):
    """
    classe abstraite representant un sport.

    Elle detient tout l'etat du score et les regles de comptage.
    Chaque sport concret (padel, tennis, badminton...) herite de cette
    classe et implemente les methodes abstraites.
    """

    nom : str
    """nom du sport (ex: "Padel")"""