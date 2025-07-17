"""
	MOUHAMED FALL : 22210185
	RANIA BENTABE : 22412390
"""
import tkinter as tk
from tkinter import ttk,messagebox
from config.Rotor import * 
from config.Reflector import *
from config.Plugboard import *
from Machine import *


def ouvrir_fenetre_chiffrement(master=None, rotor_value="", plugboard_value="", start_position_value="", reflector_value="B"):
	# Créer la fenêtre principale si aucune racine n'est fournie
	created_root = False
	if master is None:
		root = tk.Tk()
		created_root = True
	else:
		root = tk.Toplevel(master)

	root.title("Encrypt/Decrypt")
	# Création du cadre principal pour la configuration de la machine
	frame = tk.Frame(root)
	frame.pack(pady=10, padx=10)

	# Label pour la section configuration
	tk.Label(frame, text="Machine Configuration:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

	# Champs de texte pour les paramètres
	tk.Label(frame, text="Rotors (e.g., I II III):").grid(row=1, column=0, sticky="w", pady=5)
	champ_rotor = tk.Entry(frame, width=35)
	champ_rotor.grid(row=1, column=1, pady=5)

	tk.Label(frame, text="Plugboard (e.g., AB CD):").grid(row=2, column=0, sticky="w", pady=5)
	champ_plugboard = tk.Entry(frame, width=35)
	champ_plugboard.grid(row=2, column=1, pady=5)

	tk.Label(frame, text="Start Position (e.g., AAA):").grid(row=3, column=0, sticky="w", pady=5)
	champ_startposition = tk.Entry(frame, width=35)
	champ_startposition.grid(row=3, column=1, pady=5)

	tk.Label(frame, text="Reflector (e.g., B):").grid(row=4, column=0, sticky="w", pady=5)
	listereflector = ["B", "C"]
	champ_reflector = ttk.Combobox(frame, values=listereflector, width=33)  # Ajusté pour correspondre aux autres champs
	champ_reflector.current(0)  # Définir la valeur par défaut
	champ_reflector.grid(row=4, column=1, pady=5)

	#champ input texte 
	tk.Label(root, text="Input Text:").pack()
	input_text = tk.Text(root, height=5, width=50)
	input_text.pack(pady=5)

	#champ outpout texte

	tk.Label(root, text="Output Text:").pack()
	output_text = tk.Text(root, height=5, width=50)
	output_text.pack(pady=5)

	#
	def encrypt_decrypt():
		# récuperer les valeurs saisies 
		rotor = champ_rotor.get().split()
		plugboard = champ_plugboard.get()
		start_position = champ_startposition.get().upper()
		reflector = champ_reflector.get()
		input_ = input_text.get("1.0",'end-1c')

		if reflector not in "B C" :
			messagebox.showerror("Erreur", "Le reflecteur doit être de type B ou C")
			return 

		
		if not rotor or not start_position or not input_text:
			messagebox.showerror("Erreur","Champ(s) requis manquant(s)")
		try:
			machine = Machine(rotor, plugboard, reflector,start_position) # Création de la machine 
			ch = machine.chiffrerTexte(input_) # récuperer le resultat du chiffrement 
			output_text.delete("1.0",'end-1c')
			output_text.insert('1.0',ch)
		except ValueError as e :
			messagebox.showerror("Erreur",e)

	# Création des boutons interactifs encrypt et decrypt
	tk.Button(root,text="Encrypt",command=encrypt_decrypt, width=12, height=1, font=("Ariel", 10, "bold"), bg="gray69", borderwidth=3, relief="ridge").pack(side="left", padx=50)
	tk.Button(root,text="Decrypt",command=encrypt_decrypt, width=12, height=1, font=("Ariel", 10, "bold"), bg="gray69", borderwidth=3, relief="ridge").pack(side="left", padx=50)

	# Pré-remplir les champs avec les valeurs reçues
	champ_rotor.insert(0, rotor_value)
	champ_plugboard.insert(0, plugboard_value)
	champ_startposition.insert(0, start_position_value)
	champ_reflector.set(reflector_value)

	# Si on a créé la fenêtre ici, on lance mainloop
	if created_root:
		root.mainloop()

# Lancer directement si exécuté seul
if __name__ == "__main__":
	ouvrir_fenetre_chiffrement()
