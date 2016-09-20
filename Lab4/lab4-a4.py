from math import sqrt

def calculate_mean_value_with_loop(number_list):
	total = 0
	for number in number_list:
		total += number
	return total/len(number_list)

def calculate_standard_deviation(number_list):
	mean_value = calculate_mean_value_with_loop(number_list)
	sum2 = 0
	for i in number_list:
		sum2 +=(i-mean_value)**2

	return sqrt((1/(len(number_list)-1))*sum2)

def read_lines_from_file(file_name):
	text_file = open(file_name, "r")
	all_rows = text_file.readlines()
	actual_rows_without_comments = []
	for row in all_rows:

		if not row.startswith("#"):
			if row.endswith("\n"):
				row = row[:-1]
			
			actual_rows_without_comments.append(int(row))

	return actual_rows_without_comments



def user_input_float_handler(prompt):
	while True:
		try:
			user_input = float(input(prompt))
			return user_input
		except:
			print("Detta är inget tal, försök igen")

def user_input_int_handler(prompt):
	while True:
		try:
			user_input = int(input(prompt))
			return user_input
		except:
			print("Detta är inget heltal, försök igen")

def my_statistic_program():
	running = True
	number_list = []
	while running:
		main_menu_user_input = user_input_int_handler("Välj ett av följande \n1. Ladda in data \n2. Beräkna medelvärdet \n3. Beräkna standardavvikelsen \n4. Avsluta \n")
		if main_menu_user_input < 1 or main_menu_user_input > 4:
			print("Fel val, försök igen med ett tal mellan 1 och 4!")

		elif main_menu_user_input == 1:
			number_list = load_file()
			print("Laddade in ", len(number_list), " tal.")

		elif main_menu_user_input == 2:
			if len(number_list) == 0:
				print ("Ladda först in en fil med data!")
			else:
				print("Medelvärdet är: ",calculate_mean_value_with_loop(number_list))
		elif main_menu_user_input == 3:
			if len(number_list) == 0:
				print ("Ladda först in en fil med data!")
			else:
				print("Standardavvikelsen är: ", calculate_standard_deviation(number_list))
		elif main_menu_user_input == 4:
			running = False

def load_file():
	not_found_file = True
	number_list = []
	user_input = ""
	while not_found_file:
		try:
			user_input = input("Ange filnamn:")
			number_list = read_lines_from_file(user_input)
			not_found_file = False
		except IOError:
			print("Filen ", user_input, " finns ej, try igen!")
		except:
			print("Fil korrupt eller felaktigt format, försök igen med en text-fil")
	return number_list

my_statistic_program()
