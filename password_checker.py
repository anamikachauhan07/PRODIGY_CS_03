import re

def check_password_strength(password):
    # Initialize criteria tracking
    score = 0
    feedback = []
    
    # 1. Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
        
    # 2. Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one uppercase letter (A-Z).")
        
    # 3. Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one lowercase letter (a-z).")
        
    # 4. Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one number (0-9).")
        
    # 5. Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_+\-\[\]\\]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (e.g., !, @, #, $, %).")
        
    # Determine strength rating based on total score
    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong 👍"
    elif score == 3:
        strength = "Medium ⚠️"
    elif score == 2:
        strength = "Weak 📉"
    else:
        strength = "Very Weak 🚨"
        
    return strength, feedback

def main():
    print("=" * 45)
    print("      🔐 PASSWORD COMPLEXITY CHECKER 🔐      ")
    print("=" * 45)
    
    while True:
        user_password = input("\nEnter a password to evaluate (or type 'exit' to quit): ")
        if user_password.lower() == 'exit':
            print("\nExiting tool. Stay secure! 🔒")
            break
            
        if not user_password:
            print("Password cannot be empty. Try again.")
            continue
            
        strength, improvements = check_password_strength(user_password)
        
        print(f"\nPassword Strength: {strength}")
        
        if improvements:
            print("\nSuggestions to improve security:")
            for suggestion in improvements:
                print(suggestion)
        else:
            print("✨ Excellent! Your password meets all security criteria.")
        print("-" * 45)

if __name__ == "__main__":
    main()