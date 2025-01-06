import re

def evaluate_password_strength(password):
    length_check = len(password) >= 8
    uppercase_check = any(char.isupper() for char in password)
    lowercase_check = any(char.islower() for char in password)
    number_check = any(char.isdigit() for char in password)
    special_char_check = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    criteria_met = sum([length_check, uppercase_check, lowercase_check, number_check, special_char_check])

    if criteria_met == 5:
        return "Strong"
    elif criteria_met >= 3:
        return "Moderate"
    else:
        return "Weak"

def main():
    print("Password Strength Checker")
    print("--------------------------")
    password = input("Enter your password: ")
    strength = evaluate_password_strength(password)
    print(f"Password Strength: {strength}")
    
    if strength == "Weak":
        print("Suggestions: Use a mix of uppercase, lowercase, numbers, special characters, and make it at least 8 characters long.")
    elif strength == "Moderate":
        print("Suggestions: Improve your password by adding more unique characters or increasing its length.")
    else:
        print("Your password is strong.")

if __name__ == "__main__":
    main()
