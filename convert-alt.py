# recieve an upper case string
# hide its meaning by converting it in to a string of unicodes
# print the secret message
# print the original message

original = input("Enter a message to hide: ")

secret = []
str_secret = []

for char in original:
    secret.append(ord(char))
print("{}".format(secret))


print("Secret Message: ", end="")
for i in secret:
    print("{}".format(i), end="")
print()


print("Original Message: ", end="")
for j in secret:
    str_secret.append(chr(j))
print("".join(str_secret))
