def pig_a_word(word):

    result = ""

    pyg = 'ay'

    vowel_list = ["a", "e", "i", "o", "u"]

    if len(word) > 0 and word.isalpha():

        first = word [0]
        new_word_vowel = word + pyg
        new_word_consonant = word[1:] + first + pyg
        
        if first in vowel_list : 
            result = new_word_vowel
            
        else:
            result = new_word_consonant
        
    else:
        result = word



    return result

def pig(string):
    word_list = string.split(' ')

    pigword_list = []

    for word in word_list:
        pigword_list.append(pig_a_word(word))

    return " ".join(pigword_list)
