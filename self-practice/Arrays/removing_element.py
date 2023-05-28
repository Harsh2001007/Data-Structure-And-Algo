import array

arr = array.array('i',[1,2,3,4,5,6,7,8,9,10])

def removeElement(arrayName,value):
    for i in range(1,len(arrayName)+1):
        if i == value:
            arrayName.remove(i)
            return arrayName
    return "removing value does not appear in array"

print(removeElement(arr,10))

# Time compleity is o(N) && space complexity is O(1)