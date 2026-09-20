lesNombres = []

for i in range(5):
    nombre = int(input(f"Enter the number {i}: "))
    lesNombres.append(nombre)



print(max(lesNombres))
print(min(lesNombres))
print(sum(lesNombres))
print(sum(lesNombres)/len(lesNombres))

n6 = int(input("Enter a sixth number: "))

if n6 in lesNombres:
    print("This number already exists")
else:
    print("it does not exist")