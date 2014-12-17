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

new_list = ["dskmfs", "nkjnfndndssdknsdnfdnsfndjsnf", "sdkfkmsmfndnfdnf"]
print longest_word(new_list)