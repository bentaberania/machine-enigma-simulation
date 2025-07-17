"""
	MOUHAMED FALL : 22210185
	RANIA BENTABE : 22412390
"""
from itertools import permutations, product
import string
from Machine import *  # La classe Machine doit implémenter chiffrerTexte()
import multiprocessing as mp

class AttackModule:
    def __init__(self, mot_clair, mot_chiffre):
        self.mot_clair = mot_clair 
        self.mot_chiffre = mot_chiffre 

    
    def permutation_cycles(mapping):
        """
        Fonction qui calcule le motif de décomposition.
        'mapping' est un dictionnaire définissant les permutations,
        par exemple A : B => A est permuté par B.
        """
        vu = set()  # ensemble des lettres déjà explorées
        cycles = []  # liste des longueurs des cycles
        for letter in mapping:
            if letter not in vu:
                cycle = []
                current = letter
                while current in mapping and current not in vu:
                    vu.add(current)
                    cycle.append(current)
                    current = mapping[current]
                cycles.append(len(cycle))
        return sorted(cycles)


    def get_indicator_mapping(mot_clair, mot_chiffre):
        """
        Extrait la permutation correspondant à l'encryption de l'indicator.
        On suppose que les 6 premières lettres contiennent l'indicator répété.
        Pour chaque i de 0 à 2, la lettre claire à la position i est mappée
        à la lettre chiffrée à la position i+3.
        """
        if len(mot_clair) != len(mot_chiffre):
            raise ValueError("Les mots clairs et chiffrés doivent avoir la même longueur.")
        if len("".join(mot_clair)) < 6:
            raise ValueError("Le message en clair doit impérativement constituer un indicator : Triplet de lettres répété.")
        indicator = mot_clair[:3]
        mapping = {}
        for i in range(3):
            mapping[indicator[i]] = mot_chiffre[i+3]
        return mapping


    def testerConfig(args):
        """
        Pour une configuration (ordre des rotors, positions initiales, réflecteur),
        simule l'encryption d'un indicator répété (ex. "AZEAZE") et extrait la permutation.
        Si le motif cyclique correspond au motif attendu, on vérifie ensuite l'encryption complète.
        """
        ordre_rotors, reflector, positions, indicator, cycles_attendus, mot_clair, mot_chiffre = args
        plugboard = ""  # Pas de plugboard dans cette démonstration
        try:
            machine = Machine(ordre_rotors, plugboard, reflector, ''.join(positions))
            # On encrypte l'indicator répété (6 lettres)
            texte_indicator = indicator + indicator
            encrypted_indicator = machine.chiffrerTexte(texte_indicator)
            # Extraction de la permutation sur les positions 4 à 6
            mapping = {indicator[i]: encrypted_indicator[i+3] for i in range(3)}
            if AttackModule.permutation_cycles(mapping) != cycles_attendus: 
                return None
            # Vérification sur le message complet si les motifs correspondent
            machine = Machine(ordre_rotors, plugboard, reflector, ''.join(positions))
            if machine.chiffrerTexte(mot_clair) == mot_chiffre:
                return (ordre_rotors, positions, reflector)
        except ValueError:
            return None
        return None

    def retrouverCle(self):
        """
        Recherche la configuration (clé de chiffrement) compatible avec le pair connu.
        On utilise la méthode des Polonais et la parallélisation pour tenir en moins d'une minute.
        On part du principe que les 6 premières lettres de mot_clair contiennent l'indicator répété.
        """
        mot_clair = self.mot_clair 
        mot_chiffre = self.mot_chiffre 
        
        # Extraction de la permutation attendue à partir de l'indicator du known pair
        mapping_attendu = AttackModule.get_indicator_mapping(mot_clair, mot_chiffre)
        cycles_attendus = AttackModule.permutation_cycles(mapping_attendu)
        indicator = mot_clair[:3]
        
        rotors_disponibles = ['I', 'II', 'III', 'IV', 'V']
        positions_initiales = string.ascii_uppercase  # A à Z
        reflectors = ["B", "C"]  # type B ou C 

        pool = mp.Pool(mp.cpu_count())
        # Génère toutes les configurations 
        config_gen = (
            (ordre_rotors, reflector, positions, indicator, cycles_attendus, mot_clair, mot_chiffre)
            for ordre_rotors in permutations(rotors_disponibles, 3)
            for reflector in reflectors
            for positions in product(positions_initiales, repeat=3)
        )
        # Traitement en parallèle avec un chunksize 
        for result in pool.imap_unordered(AttackModule.testerConfig, config_gen, chunksize=1000):
            if result is not None:
                pool.terminate()  # On interrompt dès qu'une solution est trouvée
                return result
        pool.close()
        pool.join()
        return None

