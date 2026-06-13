def calculate_bmi():
    print("\n=========================================")
    print("      WELCOME TO THE BMI CALCULATOR      ")
    print("=========================================\n")
    
    try:
        weight = float(input("Enter your weight in kilograms (e.g., 62): "))
        height = float(input("Enter your height in meters (e.g., 1.77): "))
        
        if weight <= 0 or height <= 0:
            print("\n❌ Error: Weight and height must be positive numbers.")
            return

        # Smart Fix: If user inputs height in cm (e.g., 177), convert it to meters (1.77)
        if height > 3.0:
            print(f"⚠️ Note: Automatically converting height from {height}cm to {height/100:.2f}m.")
            height = height / 100

        # Calculate BMI
        bmi = weight / (height ** 2)
        
        print("\n-----------------------------------------")
        print(f"📊 Your Calculated BMI is: {bmi:.2f}")

        if bmi < 18.5:
            category = "Underweight"
            advice = "Consider consulting a healthcare provider for advice on nutrition."
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            advice = "Great job! Maintain your current healthy lifestyle."
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            advice = "Consider balanced dieting and regular physical activity."
        else:
            category = "Obese"
            advice = "It is highly recommended to seek medical/nutritional guidance."

        print(f"📌 Category: {category}")
        print(f"💡 Health Tip: {advice}")
        print("-----------------------------------------")
        
    except ValueError:
        print("\n❌ Error: Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    calculate_bmi()