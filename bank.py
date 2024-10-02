money = input("Enter a greeting: ").lower().strip()
if money.startswith("hello"):
    print("$0")
elif money.startswith("h"):
    print("$20")
else:
    print("$100")