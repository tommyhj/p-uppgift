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
print(number_list)
