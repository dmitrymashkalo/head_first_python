# Description:
# The third and final version of a program that displays non-repeating vowels found in a word entered by the user.

vowels = ['a', 'e', 'i', 'o', 'u']
found = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
        }

word = input('Provide a word to search for vowels: ')

for i in word:
    if i in vowels:
        found[i] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')