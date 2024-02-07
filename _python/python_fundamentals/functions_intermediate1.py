import random
def randInt(min= 0  , max= 100  ):
	if min > max:
		print("please make sure max is greater than min")
		return False
	if max < 0:
		print("please make sure max is a positive number greater than 0")
		return False
	num = random.random() * max + min
	return round(num)
#should print a random integer between 0 to 100
print(randInt())
"""random100 = randInt()
count = 0
while random100 != 99:
	random100 = randInt()
	count += 1
print(random100,"after",count) 
"""
print(randInt(max=50))		# should print a random integer between 0 to 50
print(randInt(min=50))		#should print a random integer between 50 to 100
print(randInt(min=50, max=500))	#should print a random integer between 50 and 500
print(randInt(max=50, min = 500)) # should return false
print(randInt(min = -20, max = -10)) # should return false
