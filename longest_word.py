my_string = "The quick brown fox jumped over the lazy dog"
list_of_words = my_string.split()
def find_longest_words(list_of_words):
    longest_word = ""
    for word in list_of_words:
        if len(word) > len(longest_word):
            longest_word = word
    print("The longest word is " + longest_word + "!")
print(list_of_words)
find_longest_words(list_of_words)
