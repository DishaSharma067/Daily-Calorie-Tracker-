# ------------------------------------------------------------
# Project Title: Daily Calorie Tracker CLI
# Name: Disha Sharma
# Date: 14 Oct 2025
# ------------------------------------------------------------

import datetime

# --- Task 1: Setup & Introduction ---
print("=" * 50)
print("🍎 Welcome to the Daily Calorie Tracker CLI 🍎")
print("This tool helps you track your meals and calories,")
print("compare against your daily calorie limit, and optionally save your report.")
print("=" * 50)

# --- Task 2: Input & Data Collection ---
meals = []
calories = []

num_meals = int(input("\nHow many meals do you want to enter today? "))

for i in range(num_meals):
    print(f"\nEnter details for Meal {i + 1}:")
    meal_name = input("Meal Name: ").strip().capitalize()
    calorie_amount = float(input("Calories (kcal): "))
    
    meals.append(meal_name)
    calories.append(calorie_amount)

# --- Task 3: Calorie Calculations ---
total_calories = sum(calories)
average_calories = total_calories / len(calories)
daily_limit = float(input("\nEnter your daily calorie limit (kcal): "))

# --- Task 4: Exceed Limit Warning System ---
if total_calories > daily_limit:
    status = "⚠️ You have exceeded your daily calorie limit!"
else:
    status = "✅ You are within your daily calorie limit. Great job!"

# --- Task 5: Neatly Formatted Output ---
print("\n" + "=" * 50)
print("📊 DAILY CALORIE REPORT 📊")
print("=" * 50)
print(f"{'Meal Name':<20}{'Calories (kcal)':>15}")
print("-" * 35)

for meal, cal in zip(meals, calories):
    print(f"{meal:<20}{cal:>15.2f}")

print("-" * 35)
print(f"{'Total:':<20}{total_calories:>15.2f}")
print(f"{'Average per meal:':<20}{average_calories:>15.2f}")
print("=" * 50)
print(status)
print("=" * 50)

# --- Task 6: Bonus - Save Session Log to File ---
save_choice = input("\nDo you want to save this report to a file? (yes/no): ").strip().lower()

if save_choice == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write("DAILY CALORIE TRACKER REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Date & Time: {datetime.datetime.now()}\n\n")
        file.write(f"{'Meal Name':<20}{'Calories (kcal)':>15}\n")
        file.write("-" * 35 + "\n")

        for meal, cal in zip(meals, calories):
            file.write(f"{meal:<20}{cal:>15.2f}\n")

        file.write("-" * 35 + "\n")
        file.write(f"{'Total:':<20}{total_calories:>15.2f}\n")
        file.write(f"{'Average per meal:':<20}{average_calories:>15.2f}\n")
        file.write("=" * 40 + "\n")
        file.write(status + "\n")

    print(f"\n✅ Report saved successfully as '{filename}'!")

print("\nThank you for using the Daily Calorie Tracker! 💪 Stay healthy!")
