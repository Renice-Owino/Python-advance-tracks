def multiple_sum():
	listOfNumbers = []
	addition = 0

	number = 0
	while number < 1000:
		if number % 3 == 0:
			listOfNumbers.append(number)
		elif number % 5 == 0:
			listOfNumbers.append(number)

		number+=1

	for y in listOfNumbers:
		addition+=y

	return addition
	#print the addition