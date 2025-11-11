# Name: Vansh Negi
# Roll No: 2501730158
# University: KR Mangalam University
# Course: B.Tech CSE (AI & ML) - Section A
# Subject: Programming for Problem Solving using Python
# Teacher: Prof. Sameer Farooq
# Project Title: Daily Calorie Tracker

# Task 1: Welcome Message
print("===================================")
print("   Welcome to Daily Calorie Tracker")
print("===================================")
print("This program helps you record your meals and calories.\n")

# Task 2: Input & Data Collection
meals = []
calories = []

num = int(input("How many meals did you eat today? "))

for i in range(num):
    meal = input(f"Enter name of meal {i+1}: ")
    cal = float(input(f"Enter calories for {meal}: "))
    meals.append(meal)
    calories.append(cal)

# Task 3: Calorie Calculations
total = sum(calories)
average = total / num

limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Limit Warning
if total > limit:
    status = "⚠️ You have crossed your daily limit!"
else:
    status = "✅ You are within your daily limit."

# Task 5: Neat Output
print("\n----------- DAILY REPORT -----------")
print("Meal Name\tCalories")
print("------------------------------------")
for i in range(num):
    print(f"{meals[i]}\t\t{calories[i]}")
print("------------------------------------")
print(f"Total:\t\t{total}")
print(f"Average:\t{average:.2f}")
print(status)
print("------------------------------------\n")

# Task 6: Save Report (Bonus)
save = input("Do you want to save this report? (yes/no): ")

if save.lower() == "yes":
    file = open("calorie_log.txt", "a")
    file.write("\n---- New Calorie Log ----\n")
    for i in range(num):
        file.write(f"{meals[i]}: {calories[i]} kcal\n")
    file.write(f"Total: {total}\n")
    file.write(f"Average: {average:.2f}\n")
    file.write(f"Status: {status}\n")
    file.close()
    print("\nReport saved as 'calorie_log.txt'")

print("\nThank you for using Daily Calorie Tracker!")
