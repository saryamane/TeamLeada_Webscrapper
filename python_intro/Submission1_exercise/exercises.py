import string

def triple_max(x, y, z):
    	# return the larger one between x, y, and z
	if (x > y):
		if (x > z):
			return x
		else:
			return z
	elif (y > z):
		return y
	else:
		return z

def reverse_list(my_list):
	len_list = len(my_list) - 1 # Needed to do, to avoid out of bound error
	new_list = []
	while(len_list >= 0):
		new_list.append(my_list[len_list])
		len_list -= 1
	return new_list

def de_duplicate_list(my_list):
	# returns the de-duplicated list
	# must preserve the original first appearance order
	new_item = []
	[new_item.append(item) for item in my_list if item not in new_item]
	return new_item

def map_to_list(my_list, n):
	# multiply every value in my_list by n
	# Use list comprehension!
	new_list = [item * n for item in my_list]
	return new_list

def list_contains_part_of(my_list, part):
	# returns a new list where the elements are form my_list, but each one also contains the part variable.
	# For example, list_contains_part_of(['aaple', 'pear', 'aaa'], "aa") would return ['aaple,' aaa'], since those 2 have "aa" in them.
	# returns empty list if no element.
	new_list = []
	[new_list.append(item) for item in my_list if part in item]
	return new_list

def longest_word(word_list):
    # returns the longest word in the word_list
    # returns empty string if no word
    max_length = 0
    for item in word_list:
    	item_length = len(item)
    	if item_length > max_length:
    		max_length = item_length
    		max_len_item = item

    return max_len_item


def is_pangram(phrase):
    # returns true if phrase is a pangram.
    # a pangram means that it contains all 26 alphabets (you can assume they're all lower case).
    ascii_value = set(string.ascii_lowercase)
    phrase_lower = ascii_value.intersection(phrase.lower())
    if phrase_lower == ascii_value:
    	return True
    else:
    	return False

def is_anagram(phrase_one, phrase_two):
    # returns true if the phrases are anagram of each other (you can assume they're all lower case).
    phrase_one = phrase_one.replace(' ','')
    phrase_two = phrase_two.replace(' ','')
    phrase1_list = list(phrase_one)
    phrase2_list = list(phrase_two)
    phrase1_list.sort()
    phrase2_list.sort()
    return (phrase1_list == phrase2_list)
