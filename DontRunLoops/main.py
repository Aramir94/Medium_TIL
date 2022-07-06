# Regular functino 
def multiply_by_2(x):
	x*2

# Lambda functinon
lambda x: x*2

# Map
def square(x):
    	return x*x
input_list = [2,3,4,5,6]

# without lambda 
result = map(square, input_list)

# Using lambda function 
result = map(lambda x: x*x, input_list)

# converting numbers into a list 
list(result) # map data --> list type

# Filter 
input_list = [2, 3, 4, 5, 10, 12, 14] 

def less_than_10(x):
    if x < 10:
        return x

# Without lambda
list(filter(less_than_10, input_list))

# using lambda function 
list(filter(lambda x: x < 10, input_list))
# Output: [2, 3, 4, 5]

# Reduce 
def addition(x,y):
    return x + y

from functools import reduce
input_list = [1, 2, 3, 4, 5]

# Without Lambda function
reduce(addition, input_list))

# With Lambda function
reduce(lambda x,y: x+y, input_list))
# Output: 15