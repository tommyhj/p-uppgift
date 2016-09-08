def temperature_calculator(number_of_years):
	#Asks user for year and what the temperatures was each month
	#Saves it in a 2d list with the year as the first element 
	#(not very nice but dicts and i presume classes are forbidden)
		i = 1
		year_list = []

		while i <= number_of_years:
			
			year = int(input("Vilket år är det " + str(i) + " året? "))
			
			month_list = []
			month_list.append(year)
			for j in range(1, 13):
				temperature = int(input("månad " + str(j) + ":"))
				month_list.append(temperature)

			year_list.append(month_list)
			i += 1
		return year_list

def print_statistics(year_list):
	#Prints out the contents in the list of lists
	#Assumes that the first element is the year
	#and the rest are temperature

	print ("Sammanställning:\n")
	for month_list in year_list:
		i = 0
		while i < 13:
			if i == 0:
				print("År ", str(month_list[i]))
			else:
				print("månad ", str(i), ": ", str(month_list[i]))
			i += 1
		print("genomsnittlig temperatur år ", str(month_list[0]), ": ", str(((sum(month_list[1:len(month_list)]))/(len(month_list)-1))), "\n\n")

number_of_years = int(input("Hur många år vill du mata in? "))
year_list = temperature_calculator(number_of_years)
print_statistics(year_list)

