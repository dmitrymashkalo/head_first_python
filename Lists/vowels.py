# Description:
# The first version of the program that prints all the vowels found in the word "Milliways", including repetitions.

vowels = ['a', 'e', 'i', 'o', 'u']

word = 'Milliways'

for i in word:
    if i in vowels:
        print(i)
