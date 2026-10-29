

class Joueur: 
    """
    **parametres**
    :param Nom: désigne le nom du joueur
    :param Prenom: désigne le prénom du joueur

    **return**
    - rien
    """
    Nom: str
    Prenom : str

    
    def __init__(self,N:str,P:str):
        self.Nom=N
        self.Prenom=P

