def filter(arr,target):
    for val in arr:
        if(val==target):
            return display_result(val)
        return False

def display_result(val):
    print(val+" is Found")
    
arr = ["one","two","three"]
filter(arr,"one")
