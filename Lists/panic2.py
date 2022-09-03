# Description:
# List methods are not the only way to work with them.
# This program has the same result as the previous version but is obtained by using square brackets.

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = "".join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)