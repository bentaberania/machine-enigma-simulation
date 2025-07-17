"""
	MOUHAMED FALL : 22210185
	RANIA BENTABE : 22412390
"""
import string
import collections

ALPHA_LABELS = string.ascii_uppercase  # 26 lettres de l'alphabet en majuscule


class Rotor:
    def __init__(self, correspondance, start_position):
        self.correspondance_str = correspondance.upper()
        self.position_actuel = start_position

        # Vérifier la longueur de la correspondance
        if len(self.correspondance_str) != 26:
            raise ValueError("Erreur : longueur de la chaîne de correspondance incorrecte")

        # Vérification que toutes les lettres sont dans l'alphabet
        for c in self.correspondance_str:
            if c not in ALPHA_LABELS:
                raise ValueError("Erreur : lettre incorrecte '{c}'")

        # Vérification du nombre d'occurrences
        occurrences = collections.Counter(self.correspondance_str)
        for lettre, count in occurrences.items():
            if count != 1:
                raise ValueError("Erreur : la lettre '{lettre}' apparaît {count} fois")

        # Vérifier la position de départ
        if (start_position < 0 or start_position >25):
        	raise ValueError("Erreur : '{start_position}' incorrecte")
        #effectuer une rotation à chaque entrée d'une lettre 

    def tourner(self,rotor_suivant=None,rotor_dernier=None):
        """Décale la position actuelle d'un cran."""
        
        if(self.position_actuel) == 25 :
        	self.position_actuel = 0 
        	if rotor_suivant is not None:
        		rotor_suivant.tourner(rotor_dernier,None)
        else:
        	self.position_actuel+=1
        #encoder une lettre sens aller 
        	
    def transformer_aller(self, letter):
        """Encode une lettre en passant par le rotor."""
        if letter not in ALPHA_LABELS:
            raise ValueError("Erreur : lettre à encoder incorrecte")
        
        index_entree = ALPHA_LABELS.index(letter)
        index_sortie = (index_entree + self.position_actuel) % 26
        return self.correspondance_str[index_sortie]
        
       #encoder une lettre send retour 
        
    def transformer_retour(self,letter):

        if letter not in ALPHA_LABELS:
            raise ValueError("Erreur : lettre à encoder incorrecte")   	
        else:
            index_letter = self.correspondance_str.index(letter)
            index=(index_letter - self.position_actuel) % 26
            return ALPHA_LABELS[index]


