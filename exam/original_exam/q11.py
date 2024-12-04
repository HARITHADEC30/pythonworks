roman_numerals = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
    11: "XI", 12: "XII", 13: "XIII", 14: "XIV", 15: "XV"
}

# Prompt the user for input
number = int(input("Enter a number between 1 and 15: "))

# Check if the number is in the range and display the Roman numeral
if 1 <= number <= 15:
    print("The Roman numeral for", number, "is:", roman_numerals[number])
else:
    print("Invalid input! Please enter a number between 1 and 15.")