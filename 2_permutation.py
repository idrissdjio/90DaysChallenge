str1 = "rioles"
str2 = "selori"

def hash_the_string(str):
    hashmap = {}
    for element in str:
        if element in hashmap:
            hashmap[element] += 1
        else:
            hashmap[element] = 1
    return hashmap

def permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    hashmap1 = hash_the_string(str1)
    hashmap2 = hash_the_string(str2)
    
    for key, value in hashmap1.items():
        if key not in hashmap2 or hashmap1[key] != hashmap2[key]:
            return False
    return True
    

# print(hash_the_string(str1))
print(permutation(str1, str2))