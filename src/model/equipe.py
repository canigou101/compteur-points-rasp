from src.model import Joueur

class Equipe:

    NomEquipe:str
    Joueurs : list[Joueur]
    
    def __init__(self, S:str):
        self.NomEquipe=S
        self.Joueurs=[]


    def ajoutJoueur(self,J:Joueur):
        self.Joueurs.append(J)