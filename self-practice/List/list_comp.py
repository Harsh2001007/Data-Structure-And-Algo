# #creating new list from other list

# prev_list = [1,2,3,4,5]
# new_list = []
# new_list2 = []
# new_list3 = []
# for i in prev_list:
#     multiply = i*2
#     new_list.append(multiply)
    
# print(new_list)

# comp_list = [i*2 for i in prev_list]
# print(comp_list)

# for i in prev_list:
#     divide = i/4
#     new_list2.append(divide)
    
# print(new_list2)

# new_list3 = [i/4 for i in prev_list]
# print(new_list3)
fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)
