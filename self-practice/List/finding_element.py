mylist = ["legs","back","biceps","chest","triceps","shoulder","core"]

target = "triceps"

def finding_element(listName,targetValue):
    for i,value in enumerate(listName):
        if value == targetValue:
            return i
        
    return "element does not exist in the listName"

print(finding_element(mylist,target))
