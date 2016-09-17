def calculate_mean_value_with_loop(number_list):
	total = 0
	for number in number_list:
		total += number
	return total/len(number_list)
print (calculate_mean_value_with_loop([1,2,3,4,5,6,7,8,9,10]))