from random import randint
import random

"Klass som skapar objekt för atomer"
class Atom:
    def __init__(self, atom, vikt, num, rad, kolumn):
        self.atom = atom
        self.vikt = vikt
        self.num = num
        self.rad = rad
        self.kolumn = kolumn

"""Funktion som returnerar en lista med atomernas namn och vikt"""
def skapaAtomlista():
    data = "H  1.00794 1 1;\
He 4.002602 1 18;\
Li 6.941 2 1;\
Be 9.012182 2 2;\
B  10.811 2 13;\
C  12.0107 2 14;\
N  14.0067 2 15;\
O  15.9994 2 16;\
F  18.9984032 2 17;\
Ne 20.1797 2 18;\
Na 22.98976928 3 1;\
Mg 24.3050 3 2;\
Al 26.9815386 3 13;\
Si 28.0855 3 14;\
P  30.973762 3 15;\
S  32.065 3 16;\
Cl 35.453 3 17;\
Ar 39.948 3 18;\
K  39.0983 4 1;\
Ca 40.078 4 2;\
Sc 44.955912 4 3;\
Ti 47.867 4 4;\
V  50.9415 4 5;\
Cr 51.9961 4 6;\
Mn 54.938045 4 7;\
Fe 55.845 4 8;\
Co 58.933195 4 9;\
Ni 58.6934 4 10;\
Cu 63.546 4 11;\
Zn 65.38 4 12;\
Ga 69.723 4 13;\
Ge 72.64 4 14;\
As 74.92160 4 15;\
Se 78.96 4 16;\
Br 79.904 4 17;\
Kr 83.798 4 18;\
Rb 85.4678 5 1;\
Sr 87.62 5 2;\
Y  88.90585 5 3;\
Zr 91.224 5 4;\
Nb 92.90638 5 5;\
Mo 95.96 5 6;\
Tc 98 5 7;\
Ru 101.07 5 8;\
Rh 102.90550 5 9;\
Pd 106.42 5 10;\
Ag 107.8682 5 11;\
Cd 112.411 5 12;\
In 114.818 5 13;\
Sn 118.710 5 14;\
Sb 121.760 5 15;\
Te 127.60 5 16;\
I  126.90447 5 17;\
Xe 131.293 5 18;\
Cs 132.9054519 6 1;\
Ba 137.327 6 2;\
La 138.90547 6 3;\
Ce 140.116 6 3;\
Pr 140.90765 6 3;\
Nd 144.242 6 3;\
Pm 145 6 3;\
Sm 150.36 6 3;\
Eu 151.964 6 3;\
Gd 157.25 6 3;\
Tb 158.92535 6 3;\
Dy 162.500 6 3;\
Ho 164.93032 6 3;\
Er 167.259 6 3;\
Tm 168.93421 6 3;\
Yb 173.054 6 3;\
Lu 174.9668 6 3;\
Hf 178.49 6 4;\
Ta 180.94788 6 5;\
W  183.84 6 6;\
Re 186.207 6 7;\
Os 190.23 6 8;\
Ir 192.217 6 9;\
Pt 195.084 6 10;\
Au 196.966569 6 11;\
Hg 200.59 6 12;\
Tl 204.3833 6 13;\
Pb 207.2 6 14;\
Bi 208.98040 6 15;\
Po 209 6 16;\
At 210 6 17;\
Rn 222 6 18;\
Fr 223 7 1;\
Ra 226 7 2;\
Ac 227 7 3;\
Th 232.03806 7 3;\
Pa 231.03588 7 3;\
U  238.02891 7 3;\
Np 237 7 3;\
Pu 244 7 3;\
Am 243 7 3;\
Cm 247 7 3;\
Bk 247 7 3;\
Cf 251 7 3;\
Es 252 7 3;\
Fm 257 7 3;\
Md 258 7 3;\
No 259 7 3;\
Lr 262 7 3;\
Rf 265 7 4;\
Db 268 7 5;\
Sg 271 7 6;\
Bh 272 7 7;\
Hs 270 7 8;\
Mt 276 7 9;\
Ds 281 7 10;\
Rg 280 7 11;\
Cn 285 7 12"
    atomlista = data.split(";")
    return atomlista


"Funktion som skapar en dictionary med atomerna och dess vikter, samt dess nummer"
def atomHash(atomlista):
    atomdict={}
    atomnr=1
    for i in atomlista:
        atom, vikt, rad, kolumn = i.split()
        atomdict[atomnr] = Atom(atom, vikt, atomnr, rad, kolumn) # Hashtabell som mappar atomnr till atomobjekt - pga. lättar med randint
        atomnr+=1
    return atomdict

def createPeriodicTable(): #skapar en tom matris som kan fyllas i med element
    emptyTable = [[[] for i in range(18)] for i in range(7)] #emptyTable[rad][kolumn]
    return emptyTable

atomlista = skapaAtomlista()
atomdict = atomHash(atomlista)

"Funktion som visar alla atomer"
def AtomProg1(dictionary):
    for i in range(1,len(dictionary)+1):
        print("("+str(i)+")",dictionary[i].atom, dictionary[i].vikt)
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

"Funktion som skriver ut det periodiska systemet i listform"
def AtomProg5(dictionary):
    periodicTable = createPeriodicTable()
    for i in range(1, len(dictionary)+1):
        #periodicTable[rad][kolumn]
        #dictionary[i].rad
        #dictionary[i].kolumn
        periodicTable[int(dictionary[i].rad)-1][int(dictionary[i].kolumn)-1].append(dictionary[i].atom+"("+str(dictionary[i].num)+")"+" ")
    print(periodicTable)

"Funktion som returnerar ett korrekt periodiskt system"
def checkAns(dictionary):
    periodicTable = createPeriodicTable()
    for i in range(1, len(dictionary)+1):
        periodicTable[int(dictionary[i].rad)-1][int(dictionary[i].kolumn)-1].append(dictionary[i].atom)
    return periodicTable

"Funktion som används för att träna på det periodiska systemet"
def AtomProg6(dictionary):
    emptyTable = createPeriodicTable()
    correctAns = checkAns(atomdict)
    TrueList = [True for i in range(15)]
    memoryList = [] #Används för att samma element inte ska kunna komma upp två gånger
    while True:
        if emptyTable == correctAns:
            break
        k = randint(1,len(dictionary))
        if k in memoryList:
            continue
        while True:
            try:
                print(emptyTable)
                print("I vilken rad finns", dictionary[k].atom)
                ansRad=int(input())
                if ansRad > 7: raise
                print("I vilken kolumn finns", dictionary[k].atom)
                ansKolumn=int(input())
                if ansRad == int(dictionary[k].rad) and ansKolumn == int(dictionary[k].kolumn):
                    emptyTable[int(dictionary[k].rad)-1][int(dictionary[k].kolumn)-1].append(dictionary[k].atom)
                    print("Korrekt!\n\n\n")
                    memoryList.append(k) #Lägg in i memoryList när elementet är avklarat.

                    """För att få rätt ordning på Lantanoiderna""" ##Kommer aldrig hit innan den buggar
                    if len(emptyTable[5][2]) == len(correctAns[5][2]):
                        emptyTable[5][2] = []
                        for i in range(len(correctAns[5][2])):
                            emptyTable[5][2].append(correctAns[5][2][i])
                            
                    """För att få rätt ordning på aktinoiderna""" ##kommer aldrig hit innan den buggar
                    if len(emptyTable[6][2]) == len(correctAns[6][2]):
                        emptyTable[6][2] = []
                        for i in range(len(correctAns[6][2])):
                            emptyTable[6][2].append(correctAns[6][2][i])
                    #lanthanoidList = []
                    #for i in range(15):
                        #funktion all om alla element är True returnerar den True annars False
                     #   if emptyTable[5][2][i] in correctAns[5][2]:
                     #       lanthanoidList.append(True)
                        
                    #emptyTable[5][2] - Lantanoiderna - Lanthanoids
                    #emptyTable[6][2] - Aktinoiderna - Actinoids
                    break
                else:
                    print("\nFel! Försök igen!\n")
            except:
                print("\nDu måste ange siffra 1-7 för rad eller 1-18 för kolumn\n")
                continue
    print(emptyTable)
    print("""
  ___________________________
||                           |
|| Grattis du klarade det!   |
||___________________________|    
 ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

""")

"""Programmet för betyget B"""
while True:
    try:
        choice = int(input("""\n\n\n
--------------MENY----------------
1. Visa alla atomer
2. Träna på atomnummer
3. Träna på atombeteckningar
4. Träna på atomvikter
5. Visa periodiska systemet
6. Träna på periodiska systemet
7. Sluta
----------------------------------
Vad vill du göra?
"""))
        if choice == 1:
            AtomProg1(atomdict)
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
            AtomProg5(atomdict)
        elif choice == 6:
            AtomProg6(atomdict)
        elif choice == 7:
            break
        else:
            print("nVälj tal mellan 1-6")
    except ValueError:
        print("\nVälj tal mellan 1-6")
        continue

