Sample runs for Daily Calorie Tracker

Sample Run - 1 Within Limit 
==================================================
  Welcome to the Daily Calorie Tracker CLI  
This tool helps you track your meals and calories,
compare against your daily calorie limit, and optionally save your report.
==================================================

How many meals do you want to enter today? 3

Enter details for Meal 1:
Meal Name: Breakfast
Calories (kcal): 350

Enter details for Meal 2:
Meal Name: Lunch
Calories (kcal): 600

Enter details for Meal 3:
Meal Name: Dinner
Calories (kcal): 500

Enter your daily calorie limit (kcal): 2000

==================================================
  DAILY CALORIE REPORT  
==================================================
Meal Name               Calories (kcal)
-----------------------------------
Breakfast                     350.00
Lunch                         600.00
Dinner                        500.00
-----------------------------------
Total:                       1450.00
Average per meal:              483.33
==================================================
  You are within your daily calorie limit. Great job!
==================================================

Do you want to save this report to a file? (yes/no): yes

  Report saved successfully as 'calorie_log_2025-10-26_12-30-10.txt'!

Thank you for using the Daily Calorie Tracker!   Stay healthy!



Sample Run - 2 Exceeds limit 
  Welcome to the Daily Calorie Tracker CLI  
This tool helps you track your meals and calories,
compare against your daily calorie limit, and optionally save your report.
==================================================

How many meals do you want to enter today? 4

Enter details for Meal 1:
Meal Name: Breakfast
Calories (kcal): 450

Enter details for Meal 2:
Meal Name: Lunch
Calories (kcal): 900

Enter details for Meal 3:
Meal Name: Snack
Calories (kcal): 300

Enter details for Meal 4:
Meal Name: Dinner
Calories (kcal): 850

Enter your daily calorie limit (kcal): 2200

==================================================
  DAILY CALORIE REPORT  
==================================================
Meal Name Calories (kcal)
-----------------------------------
Breakfast 450.00
Lunch 900.00
Snack 300.00
Dinner 850.00
-----------------------------------
Total: 2500.00
Average per meal: 625.00
==================================================
  You have exceeded your daily calorie limit!
==================================================

Do you want to save this report to a file? (yes/no): yes

  Report saved successfully as 'calorie_log_2025-10-26_12-35-55.txt'!

Thank you for using the Daily Calorie Tracker!   Stay healthy!


Sample Run -3 Minimal meals 

  Welcome to the Daily Calorie Tracker CLI  
This tool helps you track your meals and calories,
compare against your daily calorie limit, and optionally save your report.
==================================================

How many meals do you want to enter today? 2

Enter details for Meal 1:
Meal Name: Lunch
Calories (kcal): 700

Enter details for Meal 2:
Meal Name: Dinner
Calories (kcal): 650

Enter your daily calorie limit (kcal): 1400

==================================================
  DAILY CALORIE REPORT  
==================================================
Meal Name Calories (kcal)
-----------------------------------
Lunch 700.00
Dinner 650.00
-----------------------------------
Total: 1350.00
Average per meal: 675.00
==================================================
  You are within your daily calorie limit. Great job!
==================================================

Do you want to save this report to a file? (yes/no): no

Report not saved. Thank you for using the tracker!
