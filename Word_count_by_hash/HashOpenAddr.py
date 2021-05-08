class HashOpenAddr:
    def __init__(self, size):
        self.size = size
        self.keys = [None]*self.size
        self.values = [0]*self.size
    
    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]
    def find_slot(self, key):
        i=self.hash_function(key)
        start=i
        while self.keys[i]!=None and self.keys[i]!=key:
            i=(i+1)%self.size
            if i == start :
                return None
        return i
    def set(self, key, value=1):
        i=self.find_slot(key)
        if i==None:
            return None
        if self.keys[i]!=None:
            self.values[i]=value
        else:
            self.keys[i]=key
            self.values[i]=value
        return key
    
    def hash_function(self, key,p=3):
        h=123
        for i in range(len(key)):
            h+=ord(key[i])
        return h%p

    def remove(self, key):
        i=self.find_slot(key)
        if self.keys[i]==None:
            return None
        j=i
        while True:
            self.keys[i]=None
            while True:
                j=(j+1)%self.size
                if self.keys[j]==None:
                    return key
                k=self.hash_function(self.keys[j])
                if not (i<k<=j or j<i<k or k<=j<i):
                    break
            self.keys[i]=self.keys[j]
            self.values[i]=self.values[j]
            i=j
                
    def search(self, key):
        i=self.find_slot(key)
        if self.keys[i]!=None:
            return self.keys[i]
        else:
            return None
    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)