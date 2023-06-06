# updating the list.

listOne = [1,2,3,4,5,6,7,8,9,10]
print(listOne)
#updating - update element on existing list:

listOne[0] = 0
print(listOne)

# inserting - insert element at certain index:

listOne.insert(1,1)
print(listOne)

# append - add element to last of list.
listOne.append(11)
print(listOne)

# extend - add another list at end of list

listTwo = [12,13,14,15]

listOne.extend(listTwo)
print(listOne)