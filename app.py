# app.py
# Author: Matias Berrio
# Food-Diet Tracker Program
# This program tracks a single meal's protein intake and estimates a total daily protein intake based on a fixed multiplier.

# Task 1: Project Folder & Initial
print("Welcome to the Food-Diet Tracker!")

# Task 2: Ask the User for Input
# Get input from the user for the meal name and the protein amount.
meal_name = input("Enter the name of the meal (e.g., Breakfast, Lunch, Snack): ")
nutrient_input = input(f"Enter the amount of protein (in grams) for {meal_name}: ")

# Task 5: Add simple error handling 
try:
    # Task 3: Convert input & perform a calculation
    # Convert input string to a floating number 
    protein_grams = float(nutrient_input)
    estimated_daily_protein = protein_grams * 3 # Calculation: assume 3 meals a day

    # Task 4: Display the result clearly
    # Output the result 
    print(f"\n--- {meal_name} Summary ---")
    print(f"You logged {protein_grams:.1f} grams of protein for this meal.")
    print(f"Based on 3 similar meals, your estimated daily protein intake would be {estimated_daily_protein:.1f} grams.")
    print("--------------------------")

except ValueError:
    # Error handling
    print("\nInvalid input. Please enter a valid number (e.g., 30.5) for the protein amount.")