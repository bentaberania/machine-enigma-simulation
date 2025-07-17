"""
	MOUHAMED FALL : 22210185
	RANIA BENTABE : 22412390
"""
import collections 
"""class Plugboard:
    def __init__ (self):
        self.wiring  = {}

    def configurerConnexions(self, connections):
        self.wiring.clear()
        for key, value in connections.items():
            if key != value and key not in self.wiring and value not in self.wiring:
                self.wiring[key] = value 
                self.wiring[value] = key 
    
    def echangeLettre(self, lettre):
        return self.wiring.get(lettre, lettre)
    

plug=Plugboard()
plug.configurerConnexions({'A' : 'Z', 'B' : 'Y'})"""

class Plugboard:
    def __init__(self):
        # Initialise le dictionnaire qui stockera les connexions entre lettres.
        # Par exemple, si A est connecté à B, alors wiring contiendra {'A': 'B', 'B': 'A'}.
        self.wiring = {}

    def configurerConnexions(self, connections):
        # Sépare la chaîne 'connections' en une liste de paires de lettres.
        # Exemple : "AB EF" devient ['AB', 'EF'].
        cx = connections.split()
        
        # Vérifie qu'on ne dépasse pas 10 connexions maximum.
        if len(cx) > 10:
            raise ValueError("10 connexions au maximum sont autorisées pour le plugboard")
        
        # Parcourt chaque paire de connexion dans la liste.
        for i in cx:
            # Vérifie que chaque paire contient exactement 2 lettres.
            if len(i) != 2:
                raise ValueError("Deux seules lettres pour une paire sont autorisées")
            
            # Crée une liaison bidirectionnelle :
            # La première lettre de la paire est connectée à la deuxième, et inversement.
            self.wiring[i[0]] = i[1]
            self.wiring[i[1]] = i[0]

        # Vérifie que chaque lettre n'est connectée qu'une seule fois.
        # collections.Counter compte le nombre d'apparitions de chaque lettre parmi les valeurs du dictionnaire.
        l = collections.Counter(self.wiring.values())
        for lettre, count in l.items():
            # Si une lettre apparaît plus d'une fois, c'est une erreur car elle est connectée à plusieurs autres lettres.
            if count > 1:
                raise ValueError("Incohérence : Une lettre ne peut pas être connectée deux fois")

    def echangeLettre(self, lettre):
        # Échange la lettre selon la configuration du plugboard.
        # Si la lettre est présente dans le dictionnaire (connectée à une autre lettre),
        # renvoie la lettre correspondante, sinon renvoie la lettre elle-même.
        return self.wiring.get(lettre, lettre)
