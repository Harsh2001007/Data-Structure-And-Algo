# Q1. >>>  create an array and traverse it.

import array

arr = array.array("i",[1,2,3,4,5])
for i in range(0,len(arr)+1):
    print(i)
    
# Q2. >> appending any value in array.

arr.append(100)
print(arr)

# Q3. >> insert value in array.

arr.insert(1,6) # arr.insert(index,value)
print(arr)

# Q4. >> extend operation.

arr2 = array.array('i',[9,8,7]) # extend function uses to merge two array.
arr.extend(arr2)
print(arr)

#pop operations

arr.pop()   #pop remove last element from array
print(arr)

#index function

t = arr.index(4)
print(t)

# reverse 

arr.reverse()
print(arr)

#buffer_info method

buffer = arr.buffer_info()
print(buffer)

#count method

count = arr.count(100)
print(count)

#conver array into string
arr2 = arr.tobytes()
print(arr2)
