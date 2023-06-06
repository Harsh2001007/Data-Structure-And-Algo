listOne = ['a','b','c','d','e']

#pop method - use to pop last element if no index is provided otherwise will remove the entered indexed value

listOne.pop(2)
print(listOne)

listOne.append("e")
print(listOne)

# delete method - delete the index element

del listOne[1:4]
print(listOne)

#remove method - remove entered elemet.

listOne.remove("a")
print(listOne)