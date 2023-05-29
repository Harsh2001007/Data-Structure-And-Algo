import numpy as np

arr1 = np.array([[1,2,3,4],[4,5,6,4],[7,8,9,11]],dtype=int)

print(arr1)

def searchElement(arrName,value):
    for i in range(len(arrName)):
        for j in range(len(arrName[0])):
            if arrName[i][j] == value:
                print(i,j)
    # print("value is not present in array")
                
                
searchElement(arr1,11)
