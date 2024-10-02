num = input("Enter a set of numbers: ")
x,y,z = num.split(" ")
n1 = float(x)
n2 = float(z)
result = 0
match y:
    case "+":
        result = n1 + n2
    case "-":
        result = n1 - n2
    case "*":
        result = n1 * n2
    case "/":
        result = n1 / n2
print(result)