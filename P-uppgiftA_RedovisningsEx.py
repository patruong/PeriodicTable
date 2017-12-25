
#------------------------#

"""
Periodiska System Program
av Patrick Truong
"""

#-------------------------#
from random import randint
import random

from tkinter import *

"""Länkar för tkinter programmering"""
# https://docs.python.org/2/library/tkinter.html
# GUI commands - http://www.tutorialspoint.com/python/python_gui_programming.htm
# Button commands - http://www.tutorialspoint.com/python/tk_button.htm
# PhotoImage - http://effbot.org/tkinterbook/photoimage.htm#note
    # Info om varför PhotoImage behöver dubbla referenser
# Python tkinter color - http://wiki.tcl.tk/16166
    # More color - http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
# Removing underlying window when using popup - http://stackoverflow.com/questions/15363923/disable-the-underlying-window-when-a-popup-is-created-in-python-tkinter
# Mer om Super()
    #http://learnpythonthehardway.org/book/ex44.html

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
La 138.90547 9 3;\
Ce 140.116 9 4;\
Pr 140.90765 9 5;\
Nd 144.242 9 6;\
Pm 145 9 7;\
Sm 150.36 9 8;\
Eu 151.964 9 9;\
Gd 157.25 9 10;\
Tb 158.92535 9 11;\
Dy 162.500 9 12;\
Ho 164.93032 9 13;\
Er 167.259 9 14;\
Tm 168.93421 9 15;\
Yb 173.054 9 16;\
Lu 174.9668 9 17;\
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
Ac 227 10 3;\
Th 232.03806 10 4;\
Pa 231.03588 10 5;\
U  238.02891 10 6;\
Np 237 10 7;\
Pu 244 10 8;\
Am 243 10 9;\
Cm 247 10 10;\
Bk 247 10 11;\
Cf 251 10 12;\
Es 252 10 13;\
Fm 257 10 14;\
Md 258 10 15;\
No 259 10 16;\
Lr 262 10 17;\
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

atomlista = skapaAtomlista()
atomdict = atomHash(atomlista)

#######################################################
###-------------------------------------------------###
###-----PROGRAM UTAN GUI----------------------------###
###-------------------------------------------------###
#######################################################



"Matis som kan fyllas med element"
def createPeriodicTable(): #skapar en tom matris som kan fyllas i med element
    emptyTable = [[[] for i in range(18)] for i in range(7)] #emptyTable[rad][kolumn]
    return emptyTable

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
                break
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
            
            """ Skulle även kunna ha använt if choice = dictionary[k].vikt
så skriv rättsvar!
else:
fel!"""
            
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

#######################################################
###-------------------------------------------------###
###------------MENYN UTAN GUI-----------------------###
###-------------------------------------------------###
#######################################################

"""Programmet för betyget B"""
"""
while True:
    try:
        choice = int(input(""""""\n\n\n
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
""""""))
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
        continue"""

######################################################
###------------------------------------------------###
###------------------GUI PROGRAMMET----------------###
###------------------------------------------------###
######################################################

"""Programmet för betyget A"""
class Application(Frame):
    def __init__(self, master):
        """ Initalize Frame. """
        super(Application, self).__init__(master) #används för att slippa göra 100x klasser
        #                                       man gör istället underklasser som anropar sakerna i överklassen (tk())
        self.grid()
        self.startmenu() 

    def startmenu(self):
        """ Skapa en startmeny """
        TITLE_FONT = ("Helvetica", 18, "bold")
        label = Label(self,
              text = "Välkommen till Periodiska Systemet",
              font = TITLE_FONT)
        #label.pack(side="top", fill="x", pady =10) #pack liknar grid
        label.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        #"""
        button1 = Button(self,
                         text = "1. Visa alla atomer",
                         command = self.Atom1)
        button1.grid(row = 1, column = 1, sticky = W)
        
        button2 = Button(self,
                         text = "2. Träna på atomnummer",
                         command = self.Atom2)
        button2.grid(row = 2, column = 1, sticky = W)
        
        button3 = Button(self,
                         text = "3. Träna på atombeteckningar",
                         command = self.Atom3)
        button3.grid(row = 3, column = 1, sticky = W)

        button4 = Button(self,
                         text = "4. Träna på atomvikter",
                         command = self.Atom4)
        button4.grid(row = 4, column = 1, sticky = W)

        button5 = Button(self,
                         text = "5. Visa Periodiska systemet",
                         command = self.Atom5)
        button5.grid(row = 5, column = 1, sticky = W)

        button6 = Button(self,
                         text = "6. Träna på periodiska systemet",
                         command = self.Atom6)
        #button6 = Button(self,
        #                 text = "6. Träna på periodiska systemet",
        #                 command = self.Atom6Top)
        button6.grid(row = 6, column = 1, sticky = W)
        #"""
        """
        for i in range(7):
            startbutton_text = ["Visa alla atomer",
                    "Träna på atomnummer",
                    "Träna på atombeteckningar",
                    "Träna på atomvikter",
                    "Visa periodiska systemet",
                    "Träna på periodiska systemet",
                    "Avsluta"]
            Button(self,
                   text = str(i+1)+". " + startbutton_text[i],
                   height = 1,
                   width = 30,
                   pady = 5,
                   relief = GROOVE
                   ).grid(row = i+1, column = 1, sticky = W)
            """


###------------AtomProg1----------------------###


    def Atom1(self):
        return(AtomProg1(atomdict))


###------------AtomProg2----------------------###

    
    def Atom2(self):
        k = randint(1, len(atomlista))
        #return(AtomProg2(atomdict, k ))

        " Gå in i fönster "
        self.topAtom2 = Toplevel()
        self.master.withdraw()

        self.topAtom2.title("Atomprogram 2")

        Q_FONT = ("Times New Roman", 18, "bold")
        Label(self.topAtom2, text = ("Vilket atomnummer har"), font = Q_FONT).grid(row = 1, column = 1, columnspan = 10, sticky = W)
        Label(self.topAtom2, text = atomdict[k].atom, font = Q_FONT).grid(row = 1, column = 11, sticky = W)
        Label(self.topAtom2, text = "?", font = Q_FONT).grid(row = 1, column = 12, sticky = W)

        self.contVar = BooleanVar()
        n = [3]
        while True:

            if n[0] == 0:
                self.Atom2Fail(k)
                break
    
            " För att få frågetexten "
            Label(self.topAtom2, text = "Du har").grid(row = 3, column = 1 , columnspan = 2, sticky = W)
            Label(self.topAtom2, text = n[0]).grid(row = 3, column = 3, sticky = W)
            Label(self.topAtom2, text = "försök kvar").grid(row = 3, column = 4, sticky = W)

            " För att få svarutan "
            self.entry = Entry(self.topAtom2, width = 7)
            Label(self.topAtom2, text = " ").grid(row = 4, column = 5, sticky = W)
            self.entry.grid(row = 5, column = 10, sticky = W)
            Label(self.topAtom2, text = " ").grid(row = 6, column = 1, sticky = W)

            " För att få svarknappen "
            self.submit_bttn = Button(self.topAtom2, text = "Submit", command = lambda x = k, y = n  : self.Atom2Submit(x, y))
            self.submit_bttn.grid(row = 6, column = 10, sticky = W)
            Label(self.topAtom2, text = " ").grid(row = 7, column = 0 , sticky = W)
        
            self.waitvar(self.contVar)



    def Atom2Submit(self,k, n):
        "Funktion för att kolla svar samt returna ngt"
        content = self.entry.get()
        try:
            if int(content) == int(atomdict[k].num):
                "Skriv korrekt stäng fönster"
                self.topDone = Toplevel()
                self.topDone.title("Grattis!")
                self.topDone.grab_set()

                self.Done = Label(self.topDone, text = "Korrekt Svar!")
                self.Done.grid(row = 1, column = 1, sticky = W)

                self.okBttn = Button(self.topDone, text = "Ok", command = self.Atom2Done)
                self.okBttn.grid( row = 2, column = 1, sticky = W)
            
                #self.master.deiconify()
                #self.topAtom2.destroy()

                self.contVar.set(True)
            
            else:
                "Uppdatera raden med försök kvar"
                n[0] -= 1
                self.contVar.set(True)
                print(content)
                print(atomdict[k].num)
                return(n) #uppdatera waitvar så borde detta funka
            
        except ValueError:
            "Skapa en ruta som meddelar Error i inmatning"
            self.topError = Toplevel()
            self.topError.title("ERROR")
            self.topError.grab_set()    #Release i Atom2Error

            self.topErrorText = Label(self.topError, text = "Error! Please try again")
            self.topErrorText.grid(row = 1, column = 1, sticky = W)

            self.OkErrorBttn = Button(self.topError, text = "Ok", command = self.Atom2Error)
            self.OkErrorBttn.grid(row = 2, column = 1, sticky = W)

    def Atom2Error(self):
        self.topError.grab_release()
        self.topError.destroy()
        
    def Atom2Done(self):
        self.master.deiconify()
        self.topAtom2.destroy()
        self.topDone.destroy()        

    def Atom2Fail(self, k):
        self.topFail = Toplevel()
        self.topFail.title("FAILURE")

        self.topFail.grab_set()

        Label(self.topFail, text = "Rätt svar är:").grid(row = 1, column = 1, sticky = W)
        Label(self.topFail, text = atomdict[k].num).grid(row = 1, column = 2, sticky = W)

        Button(self.topFail, text = "Ok", command = self.Atom2FailDone).grid(row = 2, column = 2, sticky = W)

    def Atom2FailDone(self):
        self.master.deiconify()
        self.topFail.destroy()
        self.topAtom2.destroy()


###------------AtomProg3----------------------###
        

    def Atom3(self):
        k = randint(1, len(atomlista))
        #return(AtomProg3(atomdict, k))

        self.topAtom3 = Toplevel()
        self.master.withdraw()

        self.topAtom3.title("Atomprogram 3")

        Q_FONT = ("Times New Roman", 18, "bold")
        Label(self.topAtom3, text = "Vilken atombeteckning har", font = Q_FONT).grid(row = 1, column = 1, columnspan = 10, sticky = W)
        Label(self.topAtom3, text = atomdict[k].num, font = Q_FONT).grid(row = 1, column = 11, sticky = W)
        Label(self.topAtom3, text = "?", font = Q_FONT).grid(row = 1, column = 12, sticky = W)

        self.contVar = BooleanVar()
        
        n = [3]

        while True:
            if n[0] == 0:
                self.Atom3Fail(k)
                break

            " För att få frågetext "
            Label(self.topAtom3, text = "Du har").grid(row = 3, column = 1, columnspan = 2, sticky = W)
            Label(self.topAtom3, text = n[0]).grid(row = 3, column = 3, sticky = W)
            Label(self.topAtom3, text = "försök kvar").grid(row = 3, column = 4, sticky = W)

            " För att få svarsturan "
            self.entry = Entry(self.topAtom3, width = 7)
            Label(self.topAtom3, text = " ").grid(row = 4, column = 5, sticky = W)
            self.entry.grid(row = 5, column = 10, sticky = W)
            Label(self.topAtom3, text = " ").grid(row = 6, column = 1, sticky = W)

            " För att få svarknappen "
            self.submit_bttn = Button(self.topAtom3, text = "Submit", command = lambda x = k, y = n : self.Atom3Submit(x, y))
            self.submit_bttn.grid(row = 6, column = 10, sticky = W)
            Label(self.topAtom3, text = " ").grid(row = 7, column = 0 , sticky = W)

            self.waitvar(self.contVar)

    def Atom3Submit(self, k ,n):

        content = self.entry.get()

        if str(content) == str(atomdict[k].atom):

            self.topDone = Toplevel()
            self.topDone.title("Grattis!")

            self.contVar.set(True)

        else:
            n[0] -= 1
            self.contVar.set(True)
            print(content)
            print(atomdict[k].atom)
            
    def Atom3Fail(self, k):
        self.topFail = Toplevel()
        self.topFail.title("FAILURE")

        self.topFail.grab_set()         #grab on a window, which will force all event to go to that window

        Label(self.topFail, text = "Rätt svar är:").grid(row = 1, column = 1, sticky = W)
        Label(self.topFail, text = atomdict[k].atom).grid(row = 1, column = 2, sticky = W)

        Button(self.topFail, text = "Ok", command = self.Atom3FailDone).grid(row = 2, column = 2, sticky = W)

    def Atom3FailDone(self): 
        self.master.deiconify()
        self.topFail.destroy()
        self.topAtom3.destroy()


###------------AtomProg4----------------------###


    def Atom4(self):
        k = randint(1, len(atomlista))

        self.topAtom4 = Toplevel()
        self.master.withdraw()
        self.topAtom4.title("Atomprogram 4")

        Q_FONT = ("Times New Roman", 18, "bold")

        "Vilken atomvikt har [atom] ?"
        Label(self.topAtom4, text = ("Vilken atomvikt har"), font = Q_FONT).grid(row = 1, column = 1, columnspan = 10, sticky = W)
        Label(self.topAtom4, text = atomdict[k].atom, font = Q_FONT).grid(row = 1, column = 11, sticky = W)
        Label(self.topAtom4, text = "?", font = Q_FONT).grid(row = 1, column = 12, sticky = W)

        wrong1 = atomdict[randint(1, len(atomdict))].vikt
        wrong2 = atomdict[randint(1, len(atomdict))].vikt
        while wrong1 == wrong2: #För att wrong1 aldrig ska vara samma som wrong2
            wrong2 = atomdict[randint(1,len(atomdict))].vikt

        anslist = [atomdict[k].vikt, wrong1, wrong2]
        random.shuffle(anslist)

        Label(self.topAtom4, text = "Välj svarsalternativ").grid(row = 2, column = 1, sticky = W)
        Label(self.topAtom4, text = "1 - "+anslist[0]).grid(row = 3, column = 1, sticky = W)
        Label(self.topAtom4, text = "2 - "+anslist[1]).grid(row = 4, column = 1, sticky = W)
        Label(self.topAtom4, text = "3 - "+anslist[2]).grid(row = 5, column = 1, sticky = W)

        Button(self.topAtom4, text = "1", height = 1, width = 2, command = lambda x = anslist[0], y = k : self.Atom4CheckAns(x, y)
               ).grid(row = 6, column = 2, sticky = W)
        Button(self.topAtom4, text = "2", height = 1, width = 2, command = lambda x = anslist[1], y = k : self.Atom4CheckAns(x, y)
               ).grid(row = 6, column = 3, sticky = W)
        Button(self.topAtom4, text = "3", height = 1, width = 2, command = lambda x = anslist[2], y = k : self.Atom4CheckAns(x, y)
               ).grid(row = 6, column = 4, sticky = W)
            #En funktion till alla button med olika invar beroende på knapp

    def Atom4CheckAns(self, x, k):
        if atomdict[k].vikt == x:
            self.topDone = Toplevel()
            self.topDone.title("Grattis!")
            self.topDone.grab_set()

            self.Done = Label(self.topDone, text = "Korrekt Svar!")
            self.Done.grid(row = 1, column = 1, sticky = W)

            self.okBttn = Button(self.topDone, text = "Ok", command = self.Atom4Done)
            self.okBttn.grid(row = 2, column = 1, sticky = W)
        else:
            self.topDone = Toplevel()
            self.topDone.title("Fail!")
            self.topDone.grab_set()

            Label(self.topDone, text = "Fel Svar!").grid(row = 1, column = 1, sticky = W)

            self.OkBttn = Button(self.topDone, text = "Ok", command = self.Atom4Done)
            self.OkBttn.grid(row = 2, column = 1, sticky = W)
            "ungefär samma som ovan"

    def Atom4Done(self):
        self.master.deiconify()
        self.topAtom4.destroy()
        self.topDone.destroy()
            
            
###------------AtomProg5----------------------###
        
    
    def Atom5(self):
        #myImage = PhotoImage(file = "domo1.gif")

        myImage = PhotoImage(file = "PTable.gif")

        # ändrar hela skärmen till bilden kan användas när gör olika windows
        #label = Label(image=myImage)
        #label.image = myImage
        #label.pack()
        #return(label)

        top = Toplevel()
        top.title("Periodiska Systemet")

        """ Dubbla referenser för image
PhotoImage objekt tas bort när de används som skräpdata.
Därför behövs dubbla referenser - mer info se länk på toppen"""
        
        label = Label(top, image = myImage)
        label.image = myImage
        label.grid()
        #label.pack() #både grid och pack är geometri-moduler och funkar.
        
        return(label)


###------------AtomProg6----------------------###

    
    def Atom6(self):
        "Fråga om atom ska finnas i detta programmet, variablerna med, använd check för att kolla om villkoren uppfylls"
        "om de uppfylls så ska check ändra på variablerna i detta programmet"

        " Få rutan att vara en pop-up"
        self.top = Toplevel()
        self.master.withdraw() #Ta bort startmenyn när programmet körs - kommer tillbaka när man klarat programmet self.master.deiconify()

        " Skapa knapparna för alla  vanliga element "
        self.buttons_dict = {}
        for i in range(18): # column
            for n in range(7): # row
                coord = str(i+1)+":"+str(n+1)
                self.coord_list=[] #Bara för att se vilka coord som finns vid inprog
                if n == 0: # för rad 1
                    if i not in (k for k in range(1,17)):
                        self.buttons_dict[coord] = Button(self.top, height = 2, width = 5,
                                                     command = lambda x = i+1, y = n+1, z = coord: self.Atom6Ext(x,y,z))
                        self.buttons_dict[coord].grid(row = n+2, column = i+2, sticky = W)
                        self.coord_list.append(coord)
                elif n == 1 or n == 2: # för rad 2 och 3
                    if i not in (k for k in range(2,12)):
                        self.buttons_dict[coord] = Button(self.top, height = 2, width = 5,
                                                     command = lambda x = i+1, y = n+1, z = coord : self.Atom6Ext(x,y,z))
                        self.buttons_dict[coord].grid(row = n+2, column = i+2, sticky = W)
                        self.coord_list.append(coord)
                else:
                    # If-satsen används eftersom sista 6 elementen inte finns i rad 7
                    if n == 6 and i in (k for k in range(12,18)):
                        pass
                    else:
                        self.buttons_dict[coord] = Button(self.top, height = 2, width = 5,
                                                     command = lambda x = i+1, y = n+1, z = coord : self.Atom6Ext(x,y,z))
                        self.buttons_dict[coord].grid(row = n+2, column = i+2, sticky = W)
                        self.coord_list.append(coord)

        #Skapa "tom" ramen
        for i in range(19):
            Button(self.top, height = 2, width = 5,
                   state = DISABLED, relief = FLAT
                   ).grid(row = 0, column = i, sticky = W)
        Button(self.top, height = 2, width = 5,
               state = DISABLED, relief = FLAT).grid(row = 2, column = 21, sticky = W)

        #" Skapa columnnummer "        
        for i in range(18):
            Button(self.top, text = i+1, height = 2, width = 5,
                   state = DISABLED, relief = GROOVE
                   ).grid(row = 1, column = i+2, sticky = W)

        #" Skapa radnummer "    
        for i in range(7):
            Button(self.top, text = i+1, height = 2, width = 5,
                   state = DISABLED, relief = GROOVE
                   ).grid(row = i+2, column = 1, sticky = W)
            
        # Skapa mellanrum mellan periodiska systemet och lantoiderna och aktiderna
        Label(self.top, text = " ").grid(row = 9, column = 2, columnspan = 20, sticky = W) 

        " Skapa knapparna för Lantoiderna och aktiderna "
        for i in range(15):
            for n in range(2):
                coord = str(i+3)+":"+str(n+9)
                self.buttons_dict[coord] = Button(self.top, height = 2, width = 5,
                                                           command = lambda x = i+3, y = n+9, z = coord: self.Atom6Ext(x,y,z))
                self.buttons_dict[coord].grid(row = n+10, column = i+4, sticky = W)

        #Knapparna för Lantoiderna (row = 9) och Aktiderna (row = 10)
        Button(self.top, text ="LANT", bg="pale violet red", height = 2, width = 5
               ).grid(row = 7, column = 4, sticky = W)
        Button(self.top, text = "AKT", bg="hot pink", height = 2, width = 5
               ).grid(row = 8, column = 4, sticky = W)
                                 
                
        
        

        # Använd dictionary för att skapa knappar
        # http://stackoverflow.com/questions/21193285/tkinter-how-to-get-button-references - om lambda

        

        # När inte alla button är true
        # kör ett funktion som frågar efter en sak!
            # Om saken är uppfylld blir knappen True
            # funktionen frågar beroende på vilka values som är false
                #Eventuell istället för false använd state = ABLED/DISABLED'

        " AVSLUTA KNAPP "
        Button(self.top, text = "Avsluta", height = 2, width = 10,  command = self.Atom6Quit
               ).grid(row = 13, column = 18, columnspan = 3, sticky = W)
        
        """TEST knapp"""
        Button(self.top, text = "TEST", bg = "red", height = 2, width = 5, command = lambda x=1, y=2: self.test(x,y)
               ).grid(row = 12, column = 0, sticky = W)



        "Programmet"

        self.contVar = BooleanVar() #används för att pausa while loopen.

        self.memList = [] #Listan används för att hålla koll på hur många rätta svar man har.
        
        while True:
            #self.update()
            Q_FONT = ("Times New Roman", 18, "bold")
            self.A_FONT = ("Times New Roman", 10, "bold")
            if len(self.memList) == len(atomdict):
                break
            self.k = randint(1, len(atomdict))
            if self.k in self.memList:
                continue
            self.memList.append(self.k)
            self.askLabel = Label(self.top, text = "\nVar ligger " + atomdict[self.k].atom + "?" ,
                  font = Q_FONT)
            self.askLabel.grid(row = 14, column = 1, rowspan = 2, columnspan = 20, sticky = W)
            #Atom6Ext() - command till Button() och som ska ändra contVar och därmed uppfylla waitvar:s villkor.
            self.waitvar(self.contVar) # Vänta tills variabeln "contVar" ändras
            self.askLabel.grid_forget() #För att textraden inte ska bugga sig när Label är olika långa
            
            
            
        """ här vid grattis du klarade det! ska vi byta till en bild med toplevel() och kanpp destroy"""
        print("""
  ___________________________
||                           |
|| Grattis du klarade det!   |
||___________________________|    
 ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

""")
        self.master.deiconify()
        
        myImage = PhotoImage(file = "domo1.gif")

        # ändrar hela skärmen till bilden kan användas när gör olika windows
        #label = Label(image=myImage)
        #label.image = myImage
        #label.pack()
        #return(label)

        self.topFinish = Toplevel()
        self.topFinish.title("GRATTIIIIIIIIISSS")

        """ Dubbla referenser för image
PhotoImage objekt tas bort när de används som skräpdata.
Därför behövs dubbla referenser - mer info se länk på toppen"""
        
        label = Label(self.topFinish, image = myImage)
        label.image = myImage
        label.grid()
        #label.pack() #både grid och pack är geometri-moduler och funkar.
        
        return(label)
        
    " Funktion för att avsluta programmet "
    def Atom6Quit(self):
        self.topSure = Toplevel()
        self.topSure.title("Avsluta")

        self.sure = Label(self.topSure, text = "Är du säker på att du vill avsluta?")
        self.sure.grid(row = 1, column = 1, columnspan = 10, sticky = W)

        self.yQuit = Button(self.topSure, text = "Ja", width = 10, command = lambda x = True : self.Atom6QuitExt(x))
        self.yQuit.grid(row = 2, column = 1, sticky = W)

        self.nQuit = Button(self.topSure, text = "Nej", width = 10, command = lambda x = False : self.Atom6QuitExt(x))
        self.nQuit.grid(row = 2, column = 3, sticky = W)

    " Funktion för att dubbelkolla om man verkligen vill avsluta "
    def Atom6QuitExt(self, var):
        if var == True:
            self.master.deiconify()
            self.top.destroy()
            self.topSure.destroy()
        else:
            self.topSure.destroy()
        
    " Funktion som kollar om man har tryckt på rätt knapp"        
    def Atom6Ext(self, x, y, coord):
        "self.k = atomen[k]"
        " x = kolumn, y = rad"
        
        print("atomdict :", atomdict[self.k].kolumn, atomdict[self.k].rad) #Endast för provkörning
        #print("Ditt val: ", x, y)
        #print("atom: ", atomdict[self.k].atom)
        print(self.buttons_dict[coord]["text"])

        """if int(atomdict[self.k].kolumn) == int(x) and int(atomdict[self.k].rad) == int(y):
            print("GRATTTTTTTTTTTTTTTTTIS")
            print(self.memList)"""

        if int(atomdict[self.k].kolumn) == int(x) and int(atomdict[self.k].rad) == int(y):
            self.buttons_dict[coord]["text"] = atomdict[self.k].atom
            self.buttons_dict[coord]["font"] = self.A_FONT
            if int(x) == 1 and int(y) == 1 or int(x) in (k for k in range(14,17)) and int(y) == 2 or int(x) in (k for k in range(15,17)) and int(y) == 3 or int(x) == 16 and int(y) == 4:
                self.buttons_dict[coord]["bg"] = "spring green"
            elif int(x) == 18:
                self.buttons_dict[coord]["bg"] = "aquamarine"
            elif int(x) == 1 and int(y) in (k for k in range(2,8)):
                self.buttons_dict[coord]["bg"] = "salmon"
            elif int(x) == 2:
                self.buttons_dict[coord]["bg"] = "moccasin"
            elif int(x) in (k for k in range(3,13)) and int(y) in (k for k in range(4,8)):
                self.buttons_dict[coord]["bg"] = "misty rose"
            elif int(x) == 13 and int(y) == 2 or int(x) == 14 and int(y) in (k for k in range(3,5)) or int(x) == 15 and int(y) in (k for k in range(4,6)) or int(x) == 16 and int(y) in (k for k in range(5,7)):
                self.buttons_dict[coord]["bg"] = "LemonChiffon2"
            elif int(x) == 13 and int(y) in (k for k in range(3,8)) or int(x) == 14 and int(y) in (k for k in range(5,8)) or int(x) == 15 and int(y) in (k for k in range(6,8)) or int(x) == 16 and int(y) == 7:
                self.buttons_dict[coord]["bg"] = "gray"
            elif int(x) == 17 and int(y) in (k for k in range(2,7)):
                self.buttons_dict[coord]["bg"] = "lemon chiffon"
            elif int(y) == 9:
                self.buttons_dict[coord]["bg"] = "pale violet red"
            elif int(y) == 10:
                self.buttons_dict[coord]["bg"] = "hot pink"
                
            self.contVar.set(True)

        print (x,y, self.k)
        
    def test(self, x, y):
        print (x,y, self.k)
    # lambda behövs när man ska anropa funktion annars funkar det inte. PRogrammet anropar funktionen vid start och knappen fungerar inte annars
    # använd StringVar() på knapparna för att visa atomen vid uppfyllt villkor



###################################
###------------MAIN-------------###
###################################
    
root = Tk()
root.title("P-Uppgift")
app = Application(root)
root.mainloop()

    

