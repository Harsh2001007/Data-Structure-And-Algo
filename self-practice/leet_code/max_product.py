

#---------------------Finding max product of two largest number------------------

def maxProduct(arr):
    maxOne = 0
    maxTwo = 0
    
    for i in arr:
        if i>maxOne:
            maxTwo = maxOne
            maxOne = i
            
        elif i>maxTwo:
            maxTwo = i
        
        
    return maxOne*maxTwo


print(maxProduct(arr=[1,6,2,3]))            