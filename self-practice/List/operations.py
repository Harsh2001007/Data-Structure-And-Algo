# concatenation:

a = [1,2,3]
b = [4,5,6]
print(a+b)

# multiplications

print(a*4)

# sum:
print(sum(a))

#min:
print(min(b))

#max:
print(max(b))

total = 0
count = 0

mylist = []

while (True):
    inp = input("enter a number :")
    if inp == "done" : break
    value = float(inp)
    mylist.append(value)    
    total = sum(mylist)
    # count = count + 1
    average = total/len(mylist)
    
print("average :",average)

