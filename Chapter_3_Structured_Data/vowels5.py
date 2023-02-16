# Description:
# The 5 version of a program that displays non-repeating vowels found in a word entered by the user.
# Using dictionaries for the vowel frequency counter.
# Using the {dict}.setdefault method

vowels = ['a', 'e', 'i', 'o', 'u']
found = {}

word = input('Provide a word to search for vowels: ')

for i in word:
    if i in vowels:
        found.setdefault(i, 0)
        found[i] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')