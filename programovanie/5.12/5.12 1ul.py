def funkcia():
    try:
        c2 = c + 1  
        print(n[:c],n[c2:])
    except:
        print("idk daco zle")

try:
    n = input("Aký text chceš upraviť: ")
    if not n.strip():
        raise ValueError()
    try:
        c = int(input("Ktoré písmeno chceš upraviť [začína sa od 0 a nie 1]: "))
        funkcia()
    except ValueError:
        print("Chyba: Zadaj platné číslo!")
except ValueError:
    print('debil?')




