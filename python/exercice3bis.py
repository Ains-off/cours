menu = {1:"Voir mes tâches", 2:"Ajouter une tâche", 3:"Supprimer une tâche", 4:"Quitter"}
mesTaches = []

while True:

  for cle, valeur in menu.items():
    print(f"{cle}. {valeur}")
  choixMenu = int(input("Choisissez: "))