#listComprehension
squares = [x**2 for x in range(1, 11)]
print("Squares of numbers from 1 to 10:", squares)
#dictionaryComprehension
squares_dict = {x: x**2 for x in range(1, 11)}
print("Dictionary of numbers and their squares:", squares_dict)
#setComprehension
squares_set = {x**2 for x in range(1, 11)}
print("Set of squares of numbers from 1 to 10:", squares_set)