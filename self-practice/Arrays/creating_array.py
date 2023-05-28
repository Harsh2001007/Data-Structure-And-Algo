# using array module:-

import array
my_array = array.array('i',[1,2,3,4,5]) #----> O(N)
print(my_array)
print(type(my_array))


# using numpy module

import numpy as np

my_numpy = np.array([1,2,3,4,5] , dtype=int)    #-----> O(N)
print(my_numpy)