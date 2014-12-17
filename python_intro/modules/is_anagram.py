def is_anagram(phrase_one, phrase_two):
    # returns true if the phrases are anagram of each other (you can assume they're all lower case).
    phrase_one = phrase_one.replace(' ','')
    phrase_two = phrase_two.replace(' ','')
    phrase1_list = list(phrase_one)
    phrase2_list = list(phrase_two)
    phrase1_list.sort()
    phrase2_list.sort()
    return (phrase1_list == phrase2_list)

val1 = 'tom marvolo riddle'
val2 = 'i am lod voldemort'

print is_anagram(val1, val2)