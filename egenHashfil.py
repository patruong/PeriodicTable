#egen hashtabell som använder sig av pythonlista
class Node: 
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data

#krockhantering med probing
class Hashtabell:
    def __init__(self, size):
        #self.dict = []  
        self.slots = [None]*size #skapar en hashtabell till storlek size, med element NIL
    def hash2(self,word, size): # Proffsig hashfunktion för N=size
        h = 0
        for i in word:
            #h = (h*155 + ord(i))%size
            h= (h+ord(i))#%size
        return h%size
    def probe(self, oldhash, size): # Används för linjär probing, om slot är upptagen ta nästa osv.
        return (oldhash+1)%size
    def put(self, key, data):
        i = self.hash2(key, len(self.slots)) #Hasha elementet

        if self.slots[i] == None: # om slot[i] är tom; lägg in noden(atomen)
            atom = Node(key, data)
            self.slots[i] = atom
        else: # annars använd linjär probe funktion för att ta nästa slot
            #if self.slots[i] == key: 
            #    self.slots[i] = atom.data
            #else:
            nextslot = self.probe(i, len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key: # Kör om  slot inte är None eller om den inte är identiskt (får ej finnas två identiska keys)
                nextslot = self.probe(nextslot, len(self.slots)) #iterera tills villkoret inte är uppfyllt
            if self.slots[nextslot] == None: # när nästa tomma kommer, lägg till
                atom = Node(key,data) 
                self.slots[nextslot] = atom
            #else:  
            #    self.slots[nextslot] = atom.data
    def get(self,key): 
        start = self.hash2(key, len(self.slots)) # sök där den borde finnas

        data = None
        stop = False
        found = False
        position = start
        while self.slots[position] != None and not found and not stop:
            if self.slots[position].key == key: # om nyckel stämmer 
                found = True
                data = self.slots[position].data
            else: # annars leta nästa ruta (probefunktion)
                position = self.probe(position, len(self.slots))
                if position == start:
                    stop = True
        return data
        
    
