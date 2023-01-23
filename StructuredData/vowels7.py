# Description:
# Find all vowels in a word using set methods.

vowels = {'a', 'e', 'i', 'o', 'u'}

word = input('Provide a word to search for vowels: ')

found = vowels.intersection(set(word))

for vowels in found:
    print(vowels)