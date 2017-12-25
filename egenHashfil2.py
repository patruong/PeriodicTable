import random

#egen hashtabell som använder sig av pythonlista
class Node: 
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data

#krockhantering med probing
class Hashtable:
    def __init__(self, size): 
        #self.dict = []  
        self.slots = [None]*size #skapar en hashtabell till storlek size, med element NIL
    def hash2(self,word, size): # Proffsig hashfunktion för N=size
        h = 0
        for i in range(len(word)):
            #h = (h*155 + ord(i))%size
            h = (h+ord(word[i]))#%size
        return h%size
    def probe(self, oldhash, size): # Används för linjär probing, om slot är upptagen ta nästa osv.
        return (oldhash+7)%size
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
        
    

#Hashtable

class Hashtabell:
    def __init__(self, size):
        self.size = size # Size should be a prime number
        self.slots = [None] * self.size # will hold key items
        self.data = [None] * self.size # will hold data values
        self.hashiter = 0
        # when we look up at key, the corresponding position in the data list will hold the associated data blue
    def hashfunction(self, word, size):
        h = 7 #primtal
        for i in range(len(word)):
            h = (h*ord(word[i]))
        return h%size
        #return word%size
        #return hash(word)%size #kom på en bättre hashfunktion
    def rehash(self, oldhash, size):
        a = random.randrange(1,3)
        if a == 1:
            return (oldhash+1)%size
        "Kvadratisk hashing"
        self.hashiter += 1
        newhash = oldhash + self.hashiter**2

        if newhash >= self.size:
            newhash = newhash%size
        return newhash        
    def put(self, key, data):
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data #replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                      self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data #replace
    def get(self,key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
              not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        self.put(key, data)
        
                    
    
    
        

