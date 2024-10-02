text = input("Enter a text: ")
for x in text:
    if x not in ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u"):
        print(x, end="")
#Move cursor to a new line
print()
