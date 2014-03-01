import myfunctions


input("Hello! Welcome to the English to PigLatin Translator! Hit Enter to begin!")

word = input('Enter a word or phrase:')

while len(word) > 0:
    print ("Your new word or phrase is:")
    print (myfunctions.pig(word))
    print ("")
    print ("Hit Enter to end,")
    word = input('Or enter another word or phrase:')

print ('Thanks for using the English to PigLatin Translator!')



