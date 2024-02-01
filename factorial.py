def factorial(num):
	#for loop, num decrements and multiplys by a new variable (answer)
	answer = 1
	
	if num == 0:
		return 1
	
	
	for x in range (num, 0, -1):
		answer = answer * x
		
	return answer

print(factorial(8))
