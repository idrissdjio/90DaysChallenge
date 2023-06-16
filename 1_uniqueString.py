MyString = "alimenet"

def unique(MyString):
    hashmap = {}
    
    for i, element in enumerate(MyString):
        if element in hashmap:
            return False
        hashmap[element] = i
    return True
    
print(unique(MyString))