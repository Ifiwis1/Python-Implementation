##Program to return if the fuel tank of one's car is full (F) or empty (E) based on the fraction of fuel available.
def main():
        fuel_level = fraction()
        if fuel_level >= 90:
            print("F")
        elif fuel_level <= 1:
            print("E")
        else:
            print(f"{fuel_level}%")

def fraction():
    while True:
        try:
            X,Y = input("Enter a fraction of the fuel level: ").split("/")
            X,Y = int(X),int(Y)
            if X > Y:
                raise ValueError
            if Y == 0:j
                raise ZeroDivisionError
            level = round(int(X)/int(Y)*100)
            return level
        except ValueError:
            print("ValueError")
        except ZeroDivisionError:
            print("ZeroDivisionError")


if __name__ == "__main__":
    main()
