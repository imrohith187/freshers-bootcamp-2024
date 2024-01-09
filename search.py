def search (string, strArray):
    for j in range(len(strArray)):
        if (strArray[j]==(string)):
            return strArray[j]+" is found"
    return "String not found"
strArray=["one","two","three"]
print(search("one",strArray))
