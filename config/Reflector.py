"""
	MOUHAMED FALL : 22210185
	RANIA BENTABE : 22412390
"""
from config.Rotor import * 
ALPHA_LABELS = string.ascii_uppercase  # 26 lettres de l'alphabet en majuscule
class Reflector:
	def __init__(self, correspondance):
			self.correspondance_str = correspondance.upper()

			# Vérifier la longueur de la correspondance
			if len(self.correspondance_str) != 26:
			    raise ValueError("Erreur : longueur de la chaîne de correspondance incorrecte")

			# Vérification que toutes les lettres sont dans l'alphabet
			for c in self.correspondance_str:
			    if c not in ALPHA_LABELS:
			    	raise ValueError("Erreur : lettre incorrecte ")
				

			# Vérification du nombre d'occurrences
			occurrences = collections.Counter(self.correspondance_str)
			for lettre, count in occurrences.items():
			    if count != 1:
			    	raise ValueError("Erreur : la lettre '{lettre}' apparaît {count} fois")
				
	def ReflecterLettre(self,lettre):
			if(lettre not in ALPHA_LABELS):
				raise ValueError("lettre incorrecte")
			indice = self.correspondance_str.index(lettre)
			return ALPHA_LABELS[indice]
			
