text = "Hello my name is rioles "
length = 23
addSpace = "%20"

def replace_space(text, length):
    spaceCount = 0
    #calculate the total space in the string
    for element in text:
        if element == ' ':
            spaceCount+=1
    
    #set the index value
    index = length + spaceCount * 2
    
    #check if available space
    if (length < len(text)):
        text[length] = ' '
    
    #replacing value with space if needed
    for i in range(length-1, -1, -1):
        if text[i] != ' ':
            text[index - 1] = text[i]
            index -= 1
        else:
            text[index - 1] = "0"
            text[index - 2] = "2"
            text[index - 3] = "%"
            index -= 3
        return text
            
    
    
print(replace_space(text, length))