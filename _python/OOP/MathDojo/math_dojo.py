class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self, num, *nums):
        self.result += num
        for number in nums:
            self.result += number
        return self

    def subtract(self, num, *nums):
        if nums:
            self.result = num if self.result == 0 else self.result - num
            for number in nums:
                self.result -= number
        else:
            self.result -=num
        return self


md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

##Testing##
###Add Method###
# Testing case 1: Adding two numbers
math_dojo = MathDojo()
print("Testing for Addition")
result = math_dojo.add(5, 3).result
print("Test case 1 result:", result)  # Expected output: 8
math_dojo.result = 0
# Testing case 2: Adding more than two numbers
result = math_dojo.add(2, 3, 4, 5).result
print("Test case 2 result:", result)  # Expected output: 14
math_dojo.result = 0
# Testing case 3: Adding a negative number
result = math_dojo.add(10, -5).result
print("Test case 3 result:", result)  # Expected output: 5
math_dojo.result = 0


###Subtract Method ###
# Testing case 1: Subtracting two numbers
print("Testing for subtraction")
result = math_dojo.subtract(10, 5).result
print("Test case 1 result:", result)  # Expected output: 5
math_dojo.result = 0
# Testing case 2: Subtracting more than two numbers
result = math_dojo.subtract(20, 5, 3, 2).result
print("Test case 2 result:", result)  # Expected output: 10
math_dojo.result = 0
# Testing case 3: Subtracting a negative number
result = math_dojo.subtract(15, -7).result
print("Test case 3 result:", result)  # Expected output: 22
math_dojo.result = 0

###subtraction and addition in chaining method###
print("testing additin and subtraction with chaining")
# Chaining example 1
result = math_dojo.add(10).subtract(5).add(3).result
print("Chaining example 1 result:", result)  # Expected output: 8
math_dojo.result = 0
# Chaining example 2
result = math_dojo.subtract(20).add(5).subtract(3).add(2).result
print("Chaining example 2 result:", result)  # Expected output: -16

math_dojo.result = 0
