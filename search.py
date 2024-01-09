def search(x,arr):
    for i in range(len(arr)):
        if(arr[i]==x):
            print("Element Found")
            break
    return 0
    
arr = [1,2,3,4,5]
search(6,arr)
