class CharLen:
    def __init__(self,arr):
        self.arr=arr
    
    def isLessThanFourChar(self,arr):
        arrFour=[]
        for val in arr:
            if(len(val)<4):
                arrFour.append(val)
        return arrFour
    
class filter:
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
    
    def filterStrings(self,arr,target):
        for val in arr:
            if(val==target):
                return val
        return False

class display:
    def __init__(self,val):
        self.val=val
    
    def displayOnTerminal(self,val):
        if(val==False):
            print("Element not Found")
            return False
        print(val+" is Found")


strarr = ["one","two","three"]
CharLenObj = CharLen(strarr)
fourCharFiltered = CharLenObj.isLessThanFourChar(CharLenObj.arr)
filterObj = filter(fourCharFiltered,"two")
filterResult = filterObj.filterStrings(filterObj.arr,filterObj.target)
displayObj = display(filterResult)
finalResult = displayObj.displayOnTerminal(displayObj.val)




# isLessThanFourChar(strarr,"three")
