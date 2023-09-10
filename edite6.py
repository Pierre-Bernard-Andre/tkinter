#!/usr/bin/python3
#-*-Coding:utf-8 -*-

import tkinter as tk
from tkinter import filedialog

def enrejistre_teks():
    kontni = chan_teks.get("1.0", "end-1c")
    non_fichye = non_fichye_entry.get()

    if kontni and non_fichye:
        non_fichye = non_fichye + ".txt" if not non_fichye.endswith(".txt") else non_fichye
        with open(non_fichye, "w") as fichye:
            fichye.write(kontni)
        message_label.config(text="Fichye a anrejistre avèk siksè.", fg="green")
    else:
        message_label.config(text="Ranpli tout chan yo!", fg="red")

fenet = tk.Tk()
fenet.title("Editè Tèks")

frame_anwo = tk.Frame(fenet)
frame_anwo.pack(pady=10)
frame_anwo.configure(bg="dark gray")  # Couleur de fond gris foncé

frame_anba = tk.Frame(fenet)
frame_anba.pack(pady=10)

chan_teks = tk.Text(frame_anwo, wrap=tk.WORD, height=10, width=40)  # Ajoute height ak width
chan_teks.pack()

frame_bouton_non_fichye = tk.Frame(frame_anba)  # Kad pou bouton "Anrejistre" ak non fichye
frame_bouton_non_fichye.pack()

non_fichye_label = tk.Label(frame_bouton_non_fichye, text="Non Fichye:")
non_fichye_label.pack(side=tk.LEFT)

non_fichye_entry = tk.Entry(frame_bouton_non_fichye)
non_fichye_entry.pack(side=tk.LEFT)

anrejistre_bouton = tk.Button(frame_bouton_non_fichye, text="Anrejistre", command=enrejistre_teks)
anrejistre_bouton.pack(side=tk.RIGHT)
anrejistre_bouton.configure(bg="green")  # Couleur de fond verte

message_label = tk.Label(fenet, text="")
message_label.pack()

fenet.mainloop()
