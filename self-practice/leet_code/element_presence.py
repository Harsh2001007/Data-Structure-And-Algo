import numpy as np

arrOne = np.array([1,2,3,4,5,6,7,8,9,10])

def elementPresent(arrayName,target):
    for i in range(len(arrayName)):
        if arrayName[i] == target:
            print("element is present on index -->",i)
    
            
elementPresent(arrOne,1)