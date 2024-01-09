def filter(arr,target):
    for val in arr:
        if(val==target):
            return display_result(val)
        return display_result(False)

def display_result(val):
    if(val==False):
        print("Element not Found")
        return 0
    print(val+" is Found")
    
arr = ["one","two","three"]
filter(arr,"one")
