from tkinter import*
import datetime
import time
def donner_heure():
    # Obtenir l'heure courante
    current_time = datetime.datetime.now().time()

    # Définir les formats d'heure en fonction du mode d'affichage sélectionné
    if mode_afficharg.get() == "12 Hour":
        time_format = "%I:%M:%S %p"
    else:
        time_format = "%H:%M:%S"

    # Afficher l'heure dans la zone de texte
    affiche_heure.config(text=current_time.strftime(time_format))
    root.after(1000, donner_heure)

def pause():
    time.sleep(10)

# Créer la fenêtre principale de l'application
root = Tk()
root.title("Affichage de l'heure")
root.geometry("400x300")

# Définir les variables pour le mode d'affichage
mode_afficharg = StringVar(value="24 Hour")


mode_label = Label(root, text="Mode d'affichage :")
mode_12 = Radiobutton(root, text="12 Hour", variable=mode_afficharg, value="12 Hour")
mode_24 = Radiobutton(root, text="24 Hour", variable=mode_afficharg, value="24 Hour")


affiche_heure = Label(root, text="", font=("TkDefaultFont", 24))
#créer bouton pause
stop = Button(root, text="pause", command=pause)
stop.place(x=90 ,y=90)

# Placer les widgets dans la fenêtre principale
mode_label.grid(row=0, column=0, sticky="W")
mode_12.grid(row=0, column=1, sticky="W")
mode_24.grid(row=0, column=2, sticky="W")
affiche_heure.grid(row=1, column=0, columnspan=3, pady=20)

# Afficher l'heure toutes les 1 secondes
root.after(1000, donner_heure)

# Démarrer la boucle d'événements de tkinter
root.mainloop()



