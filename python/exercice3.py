Menu = {1:"Voir mes tâches", 2:"Ajouter une tâche", 3:"Supprimer une tâche", 4:"Quitter"}
mesTaches = ["vide"]
while True:
  choixMenu = int(input("Choisissez: "))

  if choixMenu == 1:
    for cle in mesTaches:
      print(f"Tâche {mesTaches.index} : {cle}")

  elif choixMenu == 2:
    while True:
      ajouter = input("ecrivez une tâche à ajouter ou tappez <quitter> pour sortir: ")
      if ajouter == "quitter":
        break
      mesTaches.append(ajouter)
      print(f"la tâche {ajouter} a été ajoutée avec succès")

  elif choixMenu == 3:
    while True:
      for cle in mesTaches:
        print(f"Tâche {mesTaches.index(cle)} : {cle}")
      supprimer = int(input("ecrivez le numéro de tâche à supprimer ou tappez <quitter> pour sortir: "))
      if supprimer == "quitter":
        break
      elif supprimer>len(mesTaches):
        print("veillez choisir un bon numéro de tâche")

      mesTaches.pop(supprimer)

  elif choixMenu == 4:
    break
  else:
    print("commande inconnu veillez ressaisir")