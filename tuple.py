# tuple is data type like arrya but it is immutable
# tuple is defined by using brackets
# tuple is used to store multiple items in a single variable
# example of tuple

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)

print(my_tuple[2])  # Accessing the third element of the tuple

# Tuples can contain different data types
mixed_tuple = (1, "Hello", 3.14, True)

print(mixed_tuple)
# Accessing elements in a mixed tuple
print(mixed_tuple[1])  # Accessing the second element (string)



tuple_with_single_element = (42,)  # Note the comma to define a single-element tuple
print(tuple_with_single_element)

# Attempting to modify a tuple will raise an error
my_tuple[0] = 10  # Uncommenting this line will raise a TypeError
# TypeError: 'tuple' object does not support item assignment 
# to modify a tuple, you need to create a new one
new_tuple = (10,) + my_tuple[1:]  # Creating a new tuple with