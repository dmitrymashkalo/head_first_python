# Description:
# The "Don't panic!" program takes this string as input and uses list methods to convert it to the string "on tap".

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()

plist.remove("'")
plist.pop(0)
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)