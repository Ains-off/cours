trouveNbr = 67
tentatives = 0
while True:
    entree = int(input("Entrez un nombre: "))
    tentatives = tentatives + 1
    if entree > trouveNbr:
        print("too high")
    elif entree < trouveNbr:
        print("too low")
    else:
        break

print(f"vous avez réussi en {tentatives} tentatives")