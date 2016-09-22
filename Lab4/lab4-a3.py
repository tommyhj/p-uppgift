from math import sqrt

def calculate_mean_value_with_loop(number_list):
	total = 0
	for number in number_list:
		total += number
	return total/len(number_list)

def standard_deviation(number_list):
	mean_value = calculate_mean_value_with_loop(number_list)
	sum2 = 0
	for i in number_list:
		sum2 +=(i-mean_value)**2

	return sqrt((1/(len(number_list)-1))*sum2)

print (standard_deviation([1,2,3,4,5,6,7,8,9,10]))