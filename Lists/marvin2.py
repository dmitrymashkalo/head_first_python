 # Using a "for" cycle with list slicing & indexing

paranoid_android = 'Marvin, the Paranoid Android'
letters = list(paranoid_android)

for i in letters[:6]:
    print('\t', i)
print()

for i in letters[-7:]:
    print('\t'*2, i)
print()

for i in letters[12:20]:
    print('\t'*3, i)