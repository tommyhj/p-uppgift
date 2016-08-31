def fuel_consumption(distance, volume):
	return (100*float(volume))/float(distance)

print("Räkna ut din bränsleförbrukning\nDetta är ett program för att räkna ut din bils bränsleförbrukning i liter per 100 km.")

distance=input("Ange körsträcka i kilometer: ")
volume=input("Ange förbrukning i liter: ")

print("Bilens bränsleförbrukning är %.3f liter/100km." %fuel_consumption(distance, volume))
