def list_contains_part_of(my_list, part):
	# returns a new list where the elements are form my_list, but each one also contains the part variable.
	# For example, list_contains_part_of(['aaple', 'pear', 'aaa'], "aa") would return ['aaple,' aaa'], since those 2 have "aa" in them.
	# returns empty list if no element.
	new_list = []
	[new_list.append(item) for item in my_list if part in item]
	return new_list

my_new_list = ['aaple', 'pear', 'aaa']
print list_contains_part_of(my_new_list, 'aa')