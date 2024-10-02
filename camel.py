name = input("Enter 2 words using camel case: ")

for i in name:
	if i.isupper():
		print("_" + i.lower(),end="")
	else:
		print(i,end="")