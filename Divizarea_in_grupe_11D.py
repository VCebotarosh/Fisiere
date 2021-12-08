suma=0
grupa1=[]
grupa2=[]

with open("H:\\VladInformatica01.10\\Lista_11_D.txt","r", encoding="utf-8") as f:
    lista=f.read().split("\n")

nume="Nume"
prenume="Prenume"
nota="Nota"
l_str="LimbaStraina"

print("   "+nume.ljust(30)+prenume.ljust(32)+nota.ljust(31)+l_str.ljust(30))

for i in range(len(lista)):
    elevi=lista[i].split()
    if(i>=9):
        print(str(i+1)+" "+str(elevi[0]).ljust(30)+str(elevi[1]).ljust(32)+str(elevi[2]).ljust(31)+str(elevi[3]).ljust(30))
    else:
        print(str(i+1)+"  "+str(elevi[0]).ljust(30)+str(elevi[1]).ljust(32)+str(elevi[2]).ljust(31)+str(elevi[3]).ljust(30))
    
    suma+=int(elevi[2])
    
    if(elevi[3]=="engl1"):
        grupa1.append(elevi)
    elif(elevi[3]=="engl2"):
        grupa2.append(elevi)

print(f"\nMedia clasei este : {suma/(len(lista))}")

with open("H:\\VladInformatica01.10\\grupa1.txt","w") as f:
    for i in range(len(grupa1)):
        f.write(" ".join(grupa1[i]))
        f.write("\n")

with open("H:\\VladInformatica01.10\\grupa2.txt","w") as f:
    for i in range(len(grupa2)):
        f.write(" ".join(grupa2[i]))
        f.write("\n")