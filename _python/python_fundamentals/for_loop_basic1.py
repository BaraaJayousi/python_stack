#Basic - print all integers from  0 to 150
print("*****Start Basic ******\n")
for num in range(151):
	print(num)

print("******* End Basic ******\n\n")


print("******** start mulitples of five ********\n")
#Multiples of five
for mult_fives in range(5,1001,5):
	print(mult_fives)


print("******** end mutliples of five *********\n\n")

print("******** start  counting the dojo way ********\n")

#Continuing the dojo way
for dojo_count in range(1,101):
	if dojo_count % 10 == 0:
		print("Coding Dojo")
		continue
	elif dojo_count % 5 == 0:
		print("Coding")
		continue
	
	print(dojo_count)

print("********** end counting the dojo way *****\n\n")


#whoa that suckers huge
print("********** start huge number sum ***************\n")
sum = 0
for num in range(500001):
	if(num % 2 != 0):
		sum += num

print(sum)

print("************ end huge number sum **************\n\n")



#count down by fours
print("******** starting count down by four *******\n")
for count in range (2018, -1, -4):
	print(count)

print("************** end count down by fours *****\n\n")




#Flexible Count
print("******** Start Flexiple counter *******\n")

low_num = 2
high_num = 9
mult = 3
for count in range (low_num, high_num + 1):
	if count % mult == 0:
		print(count)
print("*********** End flixiple counter *******\n\n")



