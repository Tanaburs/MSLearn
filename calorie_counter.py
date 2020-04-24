date = input("Enter today's date: ")
breakfast = int(input("Enter Breakfast calories: "))
lunch = int(input("Enter Lunch calories: "))
dinner = int(input("Enter Dinner calories: "))
snack = int(input("Enter Snack calories: "))
total_calories = breakfast + lunch + dinner + snack
print("Calorie count for " + date + ": " + str(total_calories))

