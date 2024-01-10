class arrAndCriteria:
    def __init__(self,arr,targetString):
        self.arr = arr
        self.targetString = targetString

def isLessThanFourChar(arr,target):
    arrFour=[]
    for val in arr:
        if(len(val)<4):
            arrFour.append(val)
    filter(arrFour,target)
    
def filter(arr,target):
    for val in arr:
        if(val==target):
            return display_result_on_terminal(val)
        return display_result_on_terminal(False)

def display_result_on_terminal(val):
    if(val==False):
        print("Element not Found")
        return False
    print(val+" is Found")


strarr = ["one","two","three"]
inputObject = arrAndCriteria(strarr,"three")
isLessThanFourChar(inputObject.arr,inputObject.targetString)
# isLessThanFourChar(strarr,"three")
