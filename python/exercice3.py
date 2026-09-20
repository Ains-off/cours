menu = {1:"Voir mes tâches", 2:"Ajouter une tâche", 3:"Supprimer une tâche", 4:"Quitter"}
mesTaches = []
while True:

  for cle, valeur in menu.items():
    print(f"{cle}. {valeur}")
  choixMenu = int(input("Choisissez: "))

  if choixMenu == 1:
    for cle, valeur in enumerate(mesTaches, start=1):
      print(f"Tâche numéro {cle} : {valeur}")

  elif choixMenu == 2:
    while True:
      ajouter = input("ecrivez une tâche à ajouter ou tappez <quitter> pour sortir: ")
      if ajouter == "quitter":
        break
      mesTaches.append(ajouter)
      print(f"la tâche {ajouter} a été ajoutée avec succès")

  elif choixMenu == 3:
    while True:
      for cle, valeur in enumerate(mesTaches, start=1):
        print(f"Tâche numéro {cle} : {valeur}")
      supprimer = int(input("ecrivez le numéro de tâche à supprimer ou tappez <0> pour sortir: "))

      if not mesTaches:
        print("la liste des taches est vide")
      elif supprimer>len(mesTaches) or supprimer<0:
        print("veillez choisir un bon numéro de tâche")
      elif supprimer == 0:
        break
      else:
        mesTaches.pop(supprimer-1)

  elif choixMenu == 4:
    break
  else:
    print("commande inconnu veillez ressaisir")