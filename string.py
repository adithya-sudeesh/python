text=input("enter a string")
old_char=input("enter the character that to be replaced")
new_char=input("enter the new character")
replaced=text.replace(old_char,new_char)
print("text after the replacement:", replaced)
str_rev=text[::-1]
print("reversed string:",str_rev)
if text == str_rev:
    print("it is palindrome")
else:
    print("it is not palindrome")
for ch in text:
    print(ch, ":", text.count(ch))
words=text.split()
print("number of words :",len(words))