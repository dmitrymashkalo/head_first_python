# Description:
# The third and final version of a program that displays non-repeating vowels found in a word entered by the user.

vowels = ['a', 'e', 'i', 'o', 'u']
found = []

word = input('Provide a word to search for vowels: ')

for i in word:
    if i in vowels:
        if i not in found:
            found.append(i)
for i in found:
    print(i)