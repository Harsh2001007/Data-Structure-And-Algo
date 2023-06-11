# List comprehension syntax --> updated_list = [i for i in already_defined_list]

listOne = [1,2,3,4,5,6,7,8,9,10]
newList = [number*2 for number in listOne]
print(newList)


# Conditonal comprehension syntax--> updated list = [i for i in already_exist_list if condition]

newListTwo = [i*i for i in listOne if i<5]
print(newListTwo)

for i in listOne:
    if i<5:
        print(i*i)
        
    else:
        pass