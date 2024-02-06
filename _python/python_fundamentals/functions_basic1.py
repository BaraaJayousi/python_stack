#1
print("####### Start - Func 1 ########")
def a():
	return 5
print(a())
print("Pridiction ==> 5")


#2
print("######## Start - Func 2 #########")
def a():
	return 5
print(a() + a())
print("Pridiction ==> 10")

#3
print("######## Start - Func 3 ########")
def a():
	return 5
	return 10
print(a())
print("Pridection ==> 5")

#4
print("######## Start - Func 4 #########")
def a():
	return 5
	print(10)
print(a())
print("Priddection ==> 5")

#5
print("######## Start - Func 5 ########")
def a():
	print(5)
x = a()
print(x)
print("Pridection ==>Terminal shows ---> 5, || the print statement shows --> None")

#6
print("######## Start - Func 6 ########")
def a(b,c):
	print(b+c)
#print(a(1,2) + a(2,3))
print("Prediction ==> None + None --> returns error due to illigeal operation===> also prints on the terimal the following 3 --> 5")


#7
print("######## Start - Func 7 ######")
def a(b,c):
	return str(b)+str(c)
print(a(2,5))
print("pridection ==>  '25'")


#8
print("######## Start - Func 8 ######")
def a():
	b = 100
	print(b)
	if b < 10:
		return 5
	else:
		return 10
	return 7
print(a())
print("pridection ==> 10")


#9
print("######## Start - Func 9 ######")
def a(b,c):
	if b<c:
		return 7
	else:
		return 14
	return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

print("pridiction ===> \n a) 7 \n b) 14 \n c) 21")


#10
print("######## Start - Func 10 ######")

def a(b,c):
	return b+c
	return 10
print(a(3,5))
print("Pridection ==> 8")

#11
print("######## Start - Func 11 ######")
b = 500
print(b)
def a():
	b = 300
	print(b)
print(b)
a()
print(b)

print("pridcection ==> \n 1) 500  \n 2) 500 \n 3) 300 \n 4) 500")


#12
print("######## Start - Func 12 ######")
b = 500
print(b)
def a():
	b = 300
	print(b)
	return b
print(b)
a()
print(b)

print("pridiction ==> \n 1) 500 \n 2) 500 \n 3) 300 \n 4) 500")



#13
print("######## Start - Func 13 ######")
b = 500
print(b)
def a():
	b = 300
	print(b)
	return b
print(b)
b=a()
print(b)

print("pridiction ==> \n 1) 500 \n 2) 500 \n 3) 300 \n 4) 300")


#14
print("######## Start - Func 14 ######")
def a():
	print(1)
	b()
	print(2)
def b():
	print(3)
a()

print("Pridiction ==>  \n 1) 1 \n 2) 3 \n 3) 2")


#15
print("######## Start - Func 15 ######")
def a():
	print(1)
	x = b()
	print(x)
	return 10
def b():
	print(3)
	return 5
y = a()
print(y)

print("pridiction ==> \n 1) 1 \n 2) 3 \n 3) 5 \n 4) 10")
