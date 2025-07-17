"""
	MOUHAMED FALL : 22210185
	RANIA BENTABE : 22412390
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

def open_encrypt_decrypt():
    try:
        subprocess.Popen(["python3", "I_chiffrement.py"])  # Lance Main.py dans un autre processus
    except Exception as e: 
        messagebox.showerror("Erreur", f"Impossible d'ouvrir la page Encrypt/Decrypt: {e}") 

def open_attack():
    try:
        subprocess.Popen(["python3", "I_Attack.py"])  # Lance Main.py dans un autre processus
    except Exception as e: 
        messagebox.showerror("Erreur", f"Impossible d'ouvrir la page Attack: {e}") 

# Création de la fenêtre principale  
root = tk.Tk() # Création de la fenêtre principale
root.title("Enigma Machine Simulator") # Titre de la fenêtre principale
root.geometry("400x500") # Taille de la fenêtre principale

# Titre
title_label = tk.Label(root, text="Enigma Machine Simulator", font=("Arial", 14, "bold")) # Création d'un label pour le titre
title_label.pack(pady=10)

# Description
desc_label = tk.Label(root, text="Explore cryptography with the Enigma machine and discover how it works", wraplength=350, justify="center")
desc_label.pack(pady=10)

try:
    image = Image.open("ressource/image")  
    image = image.resize((220, 250))  
    photo = ImageTk.PhotoImage(image)

    # Afficher l'image dans le Label Tkinter
    img_label = tk.Label(root, image=photo) # Création d'un label pour afficher l'image
    img_label.image = photo  # Garde une référence pour éviter la suppression par le garbage collector
    img_label.pack()
except Exception as e:
    print("Image non trouvée :", e)

# Boutons
btn_frame = tk.Frame(root) # Créer un cadre pour les boutons (contenu)
btn_frame.pack(pady=50)  # espace vertical

btn_encrypt_decrypt = tk.Button(btn_frame, text="Encrypt/Decrypt", command=open_encrypt_decrypt, width=17, height=2, font=("Ariel", 10, "bold"), bg="gray69", borderwidth=3, relief="ridge")
btn_encrypt_decrypt.pack(side="left", padx=20)  # espace horizontal

# Bouton Launch Attack
btn_attack = tk.Button(btn_frame, text="Launch Attack", command=open_attack, width=17, height=2, font=("Ariel", 10, "bold"), bg="gray69", borderwidth=3, relief="ridge")
btn_attack.pack(side="left", padx=20)  

# Lancer la boucle principale
root.mainloop()
