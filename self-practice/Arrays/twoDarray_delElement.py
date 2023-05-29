import numpy as np

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int)
print(arr1)

def delElement(arrName,rowIndex,colIndex):
    if rowIndex >=len(arrName) or colIndex >=len(arrName[0]):
        print("wrong inputs")
        
    else:
        arrName = np.delete(arrName,rowIndex,colIndex)
        print(arrName)
        
delElement(arr1,2,1)

#np.delete(array_name,index_to_delete,axis-->0-row and 1-column)