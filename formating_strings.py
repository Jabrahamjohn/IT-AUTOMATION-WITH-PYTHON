# using the format() method

# "base string with {} placeholders".format(variables)
example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

#Outputs:
#this is an example of using the format() method on a string


#If the placeholders indicate a number, they’re replaced by the variable corresponding to that order (starting at zero).

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

#Outputs:
#apple carrot banana

