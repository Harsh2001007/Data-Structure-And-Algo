import numpy as np

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int)
# print(arr1)

def accessElement(arrName,rowIndex,colIndex):
    
    if rowIndex >= len(arrName) or colIndex >= len(arrName):
        print("incorrect indeces")
        
    else:
        print("The index is -->",arrName[rowIndex][colIndex])
        
        
accessElement(arr1,1,2)