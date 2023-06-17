myString = "elilerr"

def palindrome_perm(myString):
    hashmap = {}
    
    for value in myString:
        #we store the char in the hashtable
        if value not in hashmap:
            hashmap[value] = 0
        hashmap[value] += 1
        
    length = len(myString)
    if (length % 2 == 0):
        for key, value in hashmap.items():
            if value % 2 != 0:
                return False
        return True
    
    else:
        for key, value in hashmap.items():
            countImpair = 0
            if value % 2 != 0:
                countImpair += 1
        if countImpair > 1:
            return False
        return True

print(palindrome_perm(myString))