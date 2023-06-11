numOfDays = int(input("enter number of days : "))

total = 0
temp_list = []
for i in range(1,numOfDays+1):
    high_temp = int(input(f"enter the highest temp of day {i}: "))
    temp_list.append(high_temp)
    total += high_temp
    
print("Total temperature : ",total)
avg = round(total/numOfDays,2)
print("average temp of entered days are :",avg)

print(temp_list)

count = 0

for temperature in temp_list:
    if (temperature > avg):
        count += 1

print("day's are above average temp",count)