class arrayAndStartCharacter:
    def __init__(self,arr,wordStartsWith):
        self.arr = arr
        self.wordStartsWith = wordStartsWith

def filter(str_inputs, predicateFn):
    result = []
    for item in str_inputs:
        if (predicateFn(item)):
            result.append(item)
    return result

def printToTerminal(array):
    for item in array:
        print(item)

def checkStringStartsWithAny(start_char):
    predicate = lambda string_item : string_item[0] == start_char
    return predicate
    
    
strings = ["Hello", "World", "Am", "Hi", "a"]
arrayObject = arrayAndStartCharacter(strings,"A")

filteredResult = filter(arrayObject.arr,checkStringStartsWithAny(arrayObject.wordStartsWith))
printToTerminal(filteredResult)
