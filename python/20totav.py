# write a program that finds the total and average  of the following list:
# Expenses= [889,788,5656,4455,455,45]
 
expenses=[889,788,5656,4455,455,45]
total=0
average=0
for i in expenses:
    total+=i
print(f"total expenses is{total}")
average=(total)/len(expenses)
print(f"total average of the given program is{average}")
