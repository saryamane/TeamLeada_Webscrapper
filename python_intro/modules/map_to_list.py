def map_to_list(my_list, n):
	# multiply every value in my_list by n
	# Use list comprehension!
	new_list = [item * n for item in my_list]
	return new_list

print map_to_list([1,2,4], 2)