import numpy as np

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int)

def traversing(arrName):
    for i in range(len(arrName)):
        for j in range(len(arrName[0])):
            print(arrName[i][j])

print(len(arr1))  
print(len(arr1[1]))          
traversing(arr1)
