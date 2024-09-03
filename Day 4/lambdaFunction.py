'''
Lambda is a keyword used to create small anonymous functions
ie. functions without a name
SYNTAX : lambda arguments : expression

arguments are the parameters the function takes
expression is the single expression that the function evaluates and returns
'''

add = lambda x,y : x + y
print(add(2,4))


# List of numbers
numbers = [1, 2, 3, 4, 5]

# Square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers) 

# Nested lambda to compute a result
result = (lambda x: (lambda y: x + y)(10))(5)
print(result)  
