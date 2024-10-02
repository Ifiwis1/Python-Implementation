def main():
    time_meal = input("What is the time now? ")
    meal_type = convert(time_meal)
    if meal_type >= 7.0 and meal_type <= 8.0:
        print("breakfast time")
    elif meal_type >= 12.0 and meal_type <= 13.0:
        print("lunch time")
    elif meal_type >= 18.0 and meal_type <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    ntime = float(hours) + (float(minutes)/60)
    return ntime

if __name__ == "__main__":
    main() 