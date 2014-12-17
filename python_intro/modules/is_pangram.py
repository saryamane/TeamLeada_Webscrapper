import string

def is_pangram(phrase):
    # returns true if phrase is a pangram.
    # a pangram means that it contains all 26 alphabets (you can assume they're all lower case).
    ascii_value = set(string.ascii_lowercase)
    phrase_lower = ascii_value.intersection(phrase.lower())
    if phrase_lower == ascii_value:
    	return True
    else:
    	return False

print is_pangram("the quick brown fox jumps over the lazy dog")