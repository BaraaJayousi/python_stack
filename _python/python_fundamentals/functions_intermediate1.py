import random
def randInt(min= 0  , max= 100  ):
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

