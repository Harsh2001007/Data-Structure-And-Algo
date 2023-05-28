import array

arr = array.array('i',[1,2,3,4,5,6,7,8,9,10])

def locateElement(arrayName,value):
    for i in range(0,len(arrayName)-1):
        if arrayName[i]==value:
            return "the index of the searched element is -->",i
    return "The searched item is not present"
            
            
print(locateElement(arr,5))

#time and spece complexity --> O(N)