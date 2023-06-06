listone = [1,2,3,4,5,6,7,"heelo",9,10.2]
print(listone)

listTwo = ["protein","cratine","biotin"]
def traversing(nameOfList):
    for i in range(len(nameOfList)):
        nameOfList[i] = nameOfList[i] + "+"
        print(nameOfList[i])
        
        
traversing(listTwo)

