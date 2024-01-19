'''
input
arr       = [18, 1, 5, 2, 10, 3]
searchKey = 2

output 
index = 3 or arr[index] --> 3
'''



def searchElement(arr, searchKey):
    """
    arr[0] == searchKey  #--> 18 == 2
    arr[1] == searchKey  #--> 1  == 2
    arr[2] == searchKey  #--> 5  == 2
    arr[3] == searchKey  #--> 2  == 2 --> element or search key found
    arr[4] == searchKey  #--> 10 == 2
    arr[5] == searchKey  #--> 3  == 2

    itr = 0                #itr = 0
    arr[itr] == searchKey  #--> 18 == 2
    itr = itr +1           #itr = 1
    arr[itr] == searchKey  #--> 1  == 2
    itr = itr +1           #itr = 2
    arr[itr] == searchKey  #--> 5  == 2
        itr = itr +1       #itr = 3
    arr[itr] == searchKey  #--> 2  == 2 --> element or search key found at itr -> 3
        itr = itr +1
    arr[itr] == searchKey  #--> 10 == 2
        itr = itr +1
    arr[itr] == searchKey  #--> 3  == 2
        itr = itr +1       --> 6
    """
    
    keyIndex = 0
    for itr in range(0, len(arr)):
        if (arr[itr] == searchKey):
            keyIndex = itr
            break
    return keyIndex

def minmumElement(arr):
    minIndex = 0
    for itr in range(0, len(arr)-1): # itr --> 0 to 5
        if (arr[minIndex] > arr[itr+1]):
            minIndex = itr+1
    return minIndex

def maxElement(arr):
    #???
    print("homework")

def bubbleSort(arr):
    print("homework")
    
def selectionSort(arr):
    #[18, 10, 5, 2, 1, 3]
    #minEle --> 1, swap with start of unsorted array
    for i in range(0, len(arr)):
        minIndex = i               # minIndex --> 0  ---> i
        for itr in range(i, len(arr)-1):
            if (arr[minIndex] > arr[itr+1]):
                minIndex = itr+1   # minIndex --> 4
                
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
        
    
    #n (means size of array) * (n-1), (n-2), (n-3) ...... 2, 1\
    #(n*(n-1))/2 -- > n to the power of 2. 
    #Complexity will be of the order of n squire. Theta of N Squire
    
    
    
    #[1, 10, 5, 2, 18, 3]
    #minEle --> 2, swap with start of unsorted array


    #[1, 2, 5, 10, 18, 3]
    #minEle --> 3, swap with start of unsorted array

    #[1, 2, 3, 10, 18, 5]
    #minEle --> 5, swap with start of unsorted array
    #[1, 2, 3, 5, 18, 10]

    #minEle --> 10, swap with start of unsorted array
    #[1, 2, 3, 5, 10, 18]
    
    

    
    
#main 
#              0  1   2  3  4  5
arr       = [18, 10, 5, 2, 1, 3]
#searchKey = 2
#index = searchElement(arr, 2)
#print("search Key : ", index, arr[index])
    
#index = minmumElement(arr)    
#print("minmumElement  : ", index, arr[index])

selectionSort(arr)
print(arr)