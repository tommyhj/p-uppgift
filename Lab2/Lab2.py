from functools import reduce
#Assignment 1:
def postage_fee(weight):
	weight = float(weight)
	rounded_weight = round(weight)
	if weight < 2:
		return (30*weight)
	elif weight >= 2 and weight < 6:
		return (28*weight) 
	elif weight >= 6 and weight < 12:
		return (25*weight)
	elif weight >= 12:
		return (23*weight)
parcel_weight = input("Ange paktetets vikt: ")
print(postage_fee(parcel_weight))

#Assignment 2:
def find_positive_numbers(number_list):
	ls = []
	for number in number_list:
		if number > 0:
			ls.append(number)

	return ls
#Assignment 2-2:
def find_positive_numbers2(number_list):
	return list(filter(lambda x: x > 0, number_list))

ls = [0, -3, 7, 2, -5, 1]
positiva = find_positive_numbers2(ls)
print (positiva)

#Assigment 3:
def sum_posistive_numbers(number_list):
	return reduce((lambda x, y: x + y), find_positive_numbers2(number_list))

ls = []
iterations = int(input("How many numbers do you want to add?"))
i = 0
while i < iterations:
	number = float(input("Add a number:"))
	ls.append(number)
	i+=1
print("The sum of the positive numbers are: ",sum_posistive_numbers(ls))