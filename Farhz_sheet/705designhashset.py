#using linked list

#with dict use defaultdict without runtime errors
class MyHashSet:

    def __init__(self):
        self.d = {}
        

    def add(self, key: int) -> None:
        self.d[key] = True
       
        

    def remove(self, key: int) -> None:
        
        try:
            self.d[key] =  False
        except:
            print()
        

    def contains(self, key: int) -> bool:
        try:
            print(self.d[key] )
            return self.d[key] != False
        except:
            return False

        
        