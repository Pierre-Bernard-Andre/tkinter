#!/usr/bin/python3
#-*-Coding:utf-8 -*-

import tkinter as tk

def ajouter_caractere(caractere):
    entree_var.set(entree_var.get() + str(caractere))

def effacer():
    entree_var.set("")

def calculer():
    try:
        resultat = eval(entree_var.get())
        entree_var.set(resultat)
    except:
        entree_var.set("Erreur")

fenetre = tk.Tk()
fenetre.title("Calculatrice")

cadre = tk.Frame(fenetre, bg='lightblue')  # Cadre en bleu pâle
cadre.grid(row=0, column=0)

entree_var = tk.StringVar()
entree = tk.Entry(cadre, textvariable=entree_var, font=('Arial', 24), justify='right', bg='lightblue')  # Couleur de fond de l'entrée
entree.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

boutons = [
    ('7', 'lightgrey'), ('8', 'lightgrey'), ('9', 'lightgrey'), ('/', 'green'),
    ('4', 'lightgrey'), ('5', 'lightgrey'), ('6', 'lightgrey'), ('*', 'orange'),
    ('1', 'lightgrey'), ('2', 'lightgrey'), ('3', 'lightgrey'), ('-', 'red'),
    ('0', 'lightgrey'), ('.', 'lightgrey'), ('=', 'lightgrey'), ('+', 'yellow'),
    ('+/-', 'lightgrey'), ('**2', 'lightgrey'), ('sqrt', 'lightgrey'), ('%', 'darkblue'), ('C', 'lightgrey')
]

row_val = 1
col_val = 0

button_width = 5  # Largeur fixe des boutons
button_height = 2  # Hauteur fixe des boutons

for bouton_text, couleur in boutons:
    if bouton_text == '=':
        tk.Button(cadre, text=bouton_text, width=button_width, height=button_height, font=('Arial', 18), command=calculer, bg=couleur).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif bouton_text == 'C':
        tk.Button(cadre, text=bouton_text, width=button_width, height=button_height, font=('Arial', 18), command=effacer, bg=couleur).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        tk.Button(cadre, text=bouton_text, width=button_width, height=button_height, font=('Arial', 18), command=lambda b=bouton_text: ajouter_caractere(b), bg=couleur).grid(row=row_val, column=col_val, padx=5, pady=5)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

fenetre.mainloop()
