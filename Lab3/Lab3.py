#Exercis 1:

def multiply(i, j, row_text):
	while j <= columns:
		numb = (i*j)
		row_text = row_text +"\t" + str(numb)
		j+=1
	return row_text

rows = int(input("Ange antal rader: "))
columns = int(input("Ange antal kolumner"))
numbers = [1,2,3,4,5,6,7,8,9]
i = 1
while i <= rows:
	if i == 1:
		row_text = multiply(i, 1, "")
		print(row_text)

	print(multiply(i, 1, str(i)))
	i+=1

#Exercise 2:
