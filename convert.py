# get input "Enter uppercase message to hide: "
secretString = ""
ostring = ""

original = input("Enter a message in uppercase: ")

# convert message into unicode


for char in original:
    secretChar = str(ord(char))
    secretString = secretString + secretChar

# print secret message as unicode

print("Secret Message: ", secretString)


# convert message back into a string

for char in range(0, len(secretString)-1, 2):
    ochar = chr(int(secretString[char] + secretString[char + 1]))
    print(type(ochar))
    ostring = ostring + str(ochar)
print("ostring type: ", type(ostring))
print("Original Message: ", ostring)

