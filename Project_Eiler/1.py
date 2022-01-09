#Progject Euler.
#Problem: numbers that are multiples of 3 and 5.

#Number multiples of 5.

number_five = []

for x in range(0,1001,5):
    number_five.append(x)
    

#Numbers multiples of three.

number_three = []

for x in range(0,1000,3):
    number_three.append(x)


#Sum list_three and list_five.

for number_five in range(len(number_five)):
    summ_five =+ number_five


for number_three in range(len(number_three)):
    summ_three =+ number_three

total = summ_three + summ_five

print("Result = ", total)