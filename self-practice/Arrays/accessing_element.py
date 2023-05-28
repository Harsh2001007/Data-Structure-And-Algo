import array

arr = array.array('i',[1,2,3,4,5,6,7,8,9,10])

def accessElement(arrayName,index):
    if index >= len(arrayName):
        print("the index value is out of range")
        
    else:
        print(arrayName[index])
        

accessElement(arr,1)

# time and space complexity - O(1)