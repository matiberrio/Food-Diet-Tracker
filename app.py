# Task 1: Welcome message
print("Welcome to the Diet Tracker!")

# Task 2: Ask for input
meal_name = input("Enter the name of the meal (e.g., Breakfast, Lunch, Snack): ")
nutrient_input = input(f"Enter the amount of protein (in grams) for {meal_name}: ")

# Task 3: Convert input & perform a calculation
protein_grams = float(nutrient_input)
estimated_daily_protein = protein_grams * 3 # Calculation: assume 3 meals per day.