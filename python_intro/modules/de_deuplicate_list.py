def de_duplicate_list(my_list):
	# returns the de-duplicated list
	# must preserve the original first appearance order
	new_item = []
	[new_item.append(item) for item in my_list if item not in new_item]
	return new_item


list_1 = [1,2,3,4,5,6,7,3,4,5]

print de_duplicate_list(list_1)