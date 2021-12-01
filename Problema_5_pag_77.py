nr_vocale=0
final=[]
vocale=["a","o","u","i","e","A","O","U","I","E"]
with open("H:\\VladInformatica01.10\\input.txt", "r") as f:
    litere=f.read()
for litera in litere:
    if litera in vocale:
        final.append(litera)
        nr_vocale+=1
with open("H:\\VladInformatica01.10\\output.txt", "w")as f:
    f.write(f"Numarul vocalelor din fisier este : {nr_vocale}")
    f.write(f"\nDaca trebuie de afisat vocalele din sir in ordine ele sunt :")
    f.write("".join(final))
print(f"Numarul de vocale este : {nr_vocale}")
print("Vocalele din fisier sunt :" ,"".join(final))