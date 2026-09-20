phrase = (input("entrez votre phrase: "))

decoupage = phrase.split()
print(len(decoupage))
print(len(phrase))
motLePlusLong = ""

for cle in decoupage:
    if int(len(cle))>int(len(motLePlusLong)):
        motLePlusLong = cle
print(motLePlusLong)

motsUniques = set(decoupage)
for cle in motsUniques:
        print(f"le mot {cle} est aparue {decoupage.count(cle)} fois")