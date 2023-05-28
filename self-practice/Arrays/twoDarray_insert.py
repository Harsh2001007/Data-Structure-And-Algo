import numpy as np

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int)
print(arr1)

insertingArray = np.insert(arr1,1,[[5,5,5]],axis=1)
print(insertingArray)

#insert(nameOfArray, index, dataToInsert, axis=1 -->column and 0 --> row)