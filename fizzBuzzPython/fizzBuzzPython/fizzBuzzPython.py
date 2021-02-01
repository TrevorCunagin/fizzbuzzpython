#created by: Trevor Cunagin
#this program prints numbers from 1 to 100, where every multiple of 3 prints
#"Fizz" and every multiple of 5 prints "Buzz". It prints "FizzBuzz" when a 
#number is a multiple of 3 and 5

for i in range(1, 101):
		if (i % 3 == 0 and i % 5 == 0): 
			print("FizzBuzz")
		elif (i % 3 == 0):
			print("Fizz")
		elif (i % 5 == 0):
			print("Buzz")
		else:
			print(i)

