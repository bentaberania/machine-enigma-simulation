"""
	MOUHAMED FALL : 22210185
	RANIA BENTABE : 22412390
"""
import tkinter as tk
from tkinter import ttk,messagebox
from Attack import *
from I_chiffrement import *



def attack():
	plain = "".join(plain_text.get("1.0",'end-1c').split()) # récupérer le texte en clair
	cipher = "".join(cipher_text.get("1.0",'end-1c').split()) #récuperer le texte chiffré
	
	
	try:
		attack = AttackModule(plain,cipher)
		ordre_rotors, positions, reflector= attack.retrouverCle()
		if(not ordre_rotors or not positions or not reflector):
			tk.messagebox.showinfo(None, "Pas de configuration trouvée !")
			return 
		rotors.delete("0",'end')
		reflectors.delete("0",'end')
		start_position.delete("0",'end')
		rotors.insert("0",ordre_rotors)
		reflectors.insert("0",reflector)
		start_position.insert("0",''.join(positions))	
	except ValueError as err:
		messagebox.showerror(None,err) 
	 
def test():
    rotor_value = rotors.get()
    plugboard_value = plugboards.get()
    start_position_value = start_position.get()
    reflector_value = reflectors.get()

    ouvrir_fenetre_chiffrement(root, rotor_value, plugboard_value, start_position_value, reflector_value)


root = tk.Tk()
root.title("Attack")

# Création du cadre principal
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

# Plain Text
tk.Label(frame, text="Plain Text:", font=("Arial", 10, "bold"), justify="center").pack(anchor="center")
plain_text = tk.Text(frame, height=5, width=50)
plain_text.pack(pady=5)

# Cipher Text
tk.Label(frame, text="Cipher Text:", font=("Arial", 10, "bold"), justify="center").pack(anchor="center")
cipher_text = tk.Text(frame, height=5, width=50)
cipher_text.pack(pady=5)

# Bouton pour démarrer l'attaque
attack_button = tk.Button(root, text="Launch Attack", command=attack, width=15, height=1, 
                          font=("Arial", 10, "bold"), bg="gray69", borderwidth=3, relief="ridge")
attack_button.pack(pady=10)

# Cadre pour afficher les détails de la clé
frame2 = tk.Frame(root)
frame2.pack(pady=10, padx=10)

# Label de section
tk.Label(frame2, text="Encryption Key Details:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

# Champs pour afficher la clé trouvée
tk.Label(frame2, text="Rotors (e.g., I II III):").grid(row=1, column=0, sticky="w", pady=5)
rotors = tk.Entry(frame2, width=35)
rotors.grid(row=1, column=1, pady=5)

tk.Label(frame2, text="Plugboard (e.g., AB CD):").grid(row=2, column=0, sticky="w", pady=5)
plugboards = tk.Entry(frame2, width=35)
plugboards.grid(row=2, column=1, pady=5)

tk.Label(frame2, text="Start Position (e.g., AAA):").grid(row=3, column=0, sticky="w", pady=5)
start_position = tk.Entry(frame2, width=35)
start_position.grid(row=3, column=1, pady=5)

tk.Label(frame2, text="Reflector (e.g., B):").grid(row=4, column=0, sticky="w", pady=5)
reflectors = tk.Entry(frame2, width=35)
reflectors.grid(row=4, column=1, pady=5)

# Bouton pour tester la clé trouvée
test_button = tk.Button(root, text="Test", command=test, width=12, height=1, 
                        font=("Arial", 10, "bold"), bg="gray69", borderwidth=3, relief="ridge")
test_button.pack(pady=10)

root.mainloop()
