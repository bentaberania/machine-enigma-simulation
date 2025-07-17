"""
	MOUHAMED FALL : 22210185
	RANIA BENTABE : 22412390
"""
from config.Rotor import * 
from config.Reflector import *
from config.Plugboard import *
import collections
import string

ALPHA_LABELS = string.ascii_uppercase  # 26 lettres de l'alphabet en majuscule

#initialiser les cinq rotors 
rotors = {
    'I': "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    'II': "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    'III': "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    'IV': "VZBRGITYUPSDNHLXAWMJQOFECK",
    'V': "VZBRGITYUPSDNHLXAWMJQOFECK"
}
	
reflectors = {
	'B' : "YRUHQSLDPXNGOKMIEBFZCWVJAT",
	'C' : "FVPJIAOYEDRZXWGCTKUQSBNMHL"
}

class Machine:
    def __init__(self, rotor, plugboard, reflector,start_position):
        # Vérifier le nombre de rotors 
        if len(rotor) != 3:
            raise ValueError("Le nombre de rotors doit être 3")
        #vérifier qu'il n'y a pas de doublons 
        r = collections.Counter(rotor)
        for x,y in r.items():
        	if(y != 1):
        		raise ValueError("Doublons non autorisés")
        #vérifier que la syntaxe est bien respectée (I II III IV V)
        for i in rotor:
        	if i not in "I II III  IV V":
        		raise ValueError("Numéro de rotor non autorisé (eg. I II III IV V)")
        #vérifier les positions initiales
        if(len(start_position)!=3):
        	raise ValueError("Une position initiale doit être donnée pour chaque rotor")
 
        self.rotor = []
        for i in range(2,-1,-1):
        	ch = rotors[rotor[i]] # récupérer la correspondance du rotor en fonction du numéro 
        	# convertir le start_position en format numérique
        	pos = ord(start_position[i])-65
        	self.rotor.append(Rotor(ch,pos))
        self.reflector = Reflector(reflectors[reflector])
        self.plugboard = Plugboard()
        self.plugboard.configurerConnexions(plugboard)
        
    def chiffrerLettre(self, lettre):
    	
        res = self.plugboard.echangeLettre(lettre)
        # traverser les rotors de droite à gauche
        
        for i in range(3):      
        	res = self.rotor[i].transformer_aller(res)
        #traverser le reflecteur 
        
        res = self.reflector.ReflecterLettre(res)
        
        #traverser les rotors au sens inverse de gauche à droite 
        
        for i in range(2,-1,-1):
        	res = self.rotor[i].transformer_retour(res)
        #traverser le plugboard
        res = self.plugboard.echangeLettre(res) 
        #tourner le rotor de doit
        self.rotor[0].tourner(self.rotor[1], self.rotor[2]) 
        return res 

    def chiffrerTexte(self, text): # chiffrer un texte 
        resultat = []
        for i in text:
            if i.upper() not in ALPHA_LABELS:
                continue
            resultat.append(self.chiffrerLettre(i.upper()))
        return "".join(resultat)



