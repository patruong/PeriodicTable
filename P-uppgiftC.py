from random import randint
import random

"Klass som skapar objekt för atomer"
class Atom:
    def __init__(self, atom, vikt, num):
        self.atom = atom
        self.vikt = vikt
        self.num = num

"""Funktion som returnerar en lista med atomernas namn och vikt"""
def skapaAtomlista():
    data = "H  1.00794;\
He 4.002602;\
Li 6.941;\
Be 9.012182;\
B  10.811;\
C  12.0107;\
N  14.0067;\
O  15.9994;\
F  18.9984032;\
Ne 20.1797;\
Na 22.98976928;\
Mg 24.3050;\
Al 26.9815386;\
Si 28.0855;\
P  30.973762;\
S  32.065;\
Cl 35.453;\
Ar 39.948;\
K  39.0983;\
Ca 40.078;\
Sc 44.955912;\
Ti 47.867;\
V  50.9415;\
Cr 51.9961;\
Mn 54.938045;\
Fe 55.845;\
Co 58.933195;\
Ni 58.6934;\
Cu 63.546;\
Zn 65.38;\
Ga 69.723;\
Ge 72.64;\
As 74.92160;\
Se 78.96;\
Br 79.904;\
Kr 83.798;\
Rb 85.4678;\
Sr 87.62;\
Y  88.90585;\
Zr 91.224;\
Nb 92.90638;\
Mo 95.96;\
Tc 98;\
Ru 101.07;\
Rh 102.90550;\
Pd 106.42;\
Ag 107.8682;\
Cd 112.411;\
In 114.818;\
Sn 118.710;\
Sb 121.760;\
Te 127.60;\
I  126.90447;\
Xe 131.293;\
Cs 132.9054519;\
Ba 137.327;\
La 138.90547;\
Ce 140.116;\
Pr 140.90765;\
Nd 144.242;\
Pm 145;\
Sm 150.36;\
Eu 151.964;\
Gd 157.25;\
Tb 158.92535;\
Dy 162.500;\
Ho 164.93032;\
Er 167.259;\
Tm 168.93421;\
Yb 173.054;\
Lu 174.9668;\
Hf 178.49;\
Ta 180.94788;\
W  183.84;\
Re 186.207;\
Os 190.23;\
Ir 192.217;\
Pt 195.084;\
Au 196.966569;\
Hg 200.59;\
Tl 204.3833;\
Pb 207.2;\
Bi 208.98040;\
Po 209;\
At 210;\
Rn 222;\
Fr 223;\
Ra 226;\
Ac 227;\
Th 232.03806;\
Pa 231.03588;\
U  238.02891;\
Np 237;\
Pu 244;\
Am 243;\
Cm 247;\
Bk 247;\
Cf 251;\
Es 252;\
Fm 257;\
Md 258;\
No 259;\
Lr 262;\
Rf 265;\
Db 268;\
Sg 271;\
Bh 272;\
Hs 270;\
Mt 276;\
Ds 281;\
Rg 280;\
Cn 285"
    atomlista = data.split(";")
    return atomlista


"Funktion som skapar en dictionary med atomerna och dess vikter, samt dess nummer"
def atomHash(atomlista):
    atomdict={}
    atomnr=1
    for i in atomlista:
        atom, vikt = i.split()
        atomdict[atomnr] = Atom(atom, vikt, atomnr) # Hashtabell som mappar atomnr till atomobjekt - pga. lättar med randint
        atomnr+=1
    return atomdict

atomlista = skapaAtomlista()
atomdict = atomHash(atomlista)

"Funktion som visar alla atomer"
def AtomProg1(atomlista):
    print(atomlista)
    
"Funktion som tränar på atomnummer"
def AtomProg2(dictionary, k):
    print("\nVilket atomnummer har", dictionary[k].atom, "?\n Du har 3 försök!")
    n=0
    while True:
        try:
            ans = int(input())
            if n == 2:
                print("\n\nDina försök är slut! Rätt svar är:", dictionary[k].num)
                break
            if ans == dictionary[k].num:
                print("Korrekt!")
                break
            else:
                print("Fel svar! Försök igen!\nVilket atomnummer har", dictionary[k].atom,"?")
                n+=1
                print("Du har", 3-n,"försök kvar!")
        except:
            print("Svaret ska vara en siffra mellan 1-112. Försök igen!\n Vilket atomnummer har", dictionary[k].atom,"?")
            continue

"Funktion som tränar på atombeteckningar"
def AtomProg3(dictionary, k):
    print("\nVilken atombeteckningar har", dictionary[k].num, "?\n Du har 3 försök!")
    n=0
    while True:
        try:
            ans = input()
            if n == 2:
                print("\n\nDina försök är slut! Rätt svar är:", dictionary[k].atom)
            if ans == dictionary[k].atom:
                print("Korrekt!")
                break
            else:
                print("Fel svar! Försök igen!\nVilken atombeteckningar har", dictionary[k].num,"?")
                n+=1
                print("Du har", 3-n,"försök kvar!")
        except:
            print("Svaret ska bestå av 1-2 bokstäver. Försök igen!\n Vilket atomnummer har", dictionary[k].num,"?")
        
"Funktion som tränar på atomvikter"
def AtomProg4(dictionary, k):
    print("\nVilken atomvikt har", dictionary[k].atom, "?")
    n=0
    ans=0
    wrong1 = dictionary[randint(1, len(atomdict))].vikt
    wrong2 = dictionary[randint(1, len(atomdict))].vikt
    anslist=[dictionary[k].vikt, wrong1, wrong2]
    random.shuffle(anslist) #Nu är anslist blandad
    while True:
        try:
            print("""
Välj svarsalternativ

1.""", anslist[0],"""
2.""", anslist[1],"""
3.""", anslist[2],"\n")
            choice = int(input())
            if choice == 1:
                ans = anslist[0]
                print("Ditt val är", choice, ":", anslist[0])
                if ans == dictionary[k].vikt:
                    print("korrekt!")
                    break
                else:
                    print("Fel val!\n\nRätt svar är", dictionary[k].vikt)
                    break
            elif choice == 2:
                ans = anslist[1]
                print("Ditt val är", choice, ":", anslist[1])
                if ans == dictionary[k].vikt:
                    print("korrekt!")
                    break
                else:
                    print("Fel val!\n\nRätt svar är", dictionary[k].vikt)
                    break
            elif choice == 3:
                ans = anslist[2]
                print("Ditt val är", choice, ":", anslist[2])
                if ans == dictionary[k].vikt:
                    print("korrekt!")
                    break
                else:
                    print("Fel val!\n\nRätt svar är", dictionary[k].vikt)
                    break
            else:
                print("Val mål vara mellan 1-3\n Vänligen försök igen!")
                print("\nVilken atomvikt har", dictionary[k].atom, "?")
        except:
            print("Val måste vara mellan 1-3\n Vänligen försök igen!")
            print("\nVilken atomvikt har", dictionary[k].atom, "?")
    

"""Programmet för betyget E"""
while True:
    try:
        choice = int(input("""\n\n\n
--------------MENY----------------
1. Visa alla atomer
2. Träna på atomnummer
3. Träna på atombeteckningar
4. Träna på atomvikter
5. Sluta
----------------------------------
Vad vill du göra?
"""))
        if choice == 1:
            AtomProg1(atomlista)
        elif choice == 2:
            k = randint(1,len(atomlista))
            AtomProg2(atomdict, k)
        elif choice == 3:
            k = randint(1,len(atomlista))
            AtomProg3(atomdict, k)
        elif choice == 4:
            k = randint(1,len(atomlista))
            AtomProg4(atomdict, k)
        elif choice == 5:
            break
        else:
            print("nVälj tal mellan 1-4")
    except ValueError:
        print("\nVälj tal mellan 1-4")
        continue

#
"""Glöm inte CSN"""
