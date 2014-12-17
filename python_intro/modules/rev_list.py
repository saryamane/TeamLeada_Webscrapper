def reverse_list(my_list):
	len_list = len(my_list) - 1 # Needed to do, to avoid out of bound error
	new_list = []
	while(len_list >= 0):
		new_list.append(my_list[len_list])
		len_list -= 1
	return new_list

list_value = [1,2,3,4,5]
new_list_value = [2, 3, 4, 1, 5, "a"]

print reverse_list(list_value)
print reverse_list(new_list_value)
