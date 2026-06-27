# 🔐 Password Complexity Checker

A Python-based Password Complexity Checker that evaluates the strength of a password based on common cybersecurity best practices. The program analyzes password length, uppercase and lowercase letters, numbers, and special characters, then provides users with a strength rating and suggestions for improvement.

This project was developed as part of the **Prodigy Infotech Cyber Security Internship (Task 03)**.

## 🚀 Features

- Checks minimum password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numeric digits
- Detects special characters
- Provides password strength rating
- Gives suggestions to improve weak passwords
- Simple command-line interface

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (`re` module)

## 📂 Project Structure

```text
PRODIGY_CS_02/
│
├── image_encryption.py
├── ima.jpg
├── encrypted.png
├── recovered.jpg
└── README.md
```

## ⚙️ How It Works

The program evaluates a password using five security criteria:

- Minimum length (8 or more characters)
- At least one uppercase letter
- At least one lowercase letter
- At least one numeric digit
- At least one special character

Each satisfied criterion increases the overall security score.

## 📦 Installation

### Clone the Repository

git clone https://github.com/anamikachauhan07/PRODIGY_CS_03.git

cd PRODIGY_CS_03

### Run the Program

```bash
python password_checker.py

## ▶️ Example

=============================================
      🔐 PASSWORD COMPLEXITY CHECKER 🔐
=============================================

Enter a password to evaluate: Password@123

Password Strength: Very Strong 💪

✨ Excellent! Your password meets all security criteria.

### Weak Password Example

Enter a password to evaluate: abc123

Password Strength: Weak 📉

Suggestions to improve security:

❌ Password should be at least 8 characters long.
❌ Include at least one uppercase letter (A-Z).
❌ Include at least one special character.


## 🔒 Password Evaluation Criteria

| Criterion | Requirement |
|-----------|-------------|
| Length | At least 8 characters |
| Uppercase | One or more uppercase letters |
| Lowercase | One or more lowercase letters |
| Number | One or more digits |
| Special Character | One or more special characters |

## 🎯 Learning Objectives

This project demonstrates:

- Password Security Principles
- Regular Expressions (Regex)
- User Input Validation
- Conditional Logic
- Command-Line Application Development
- Cybersecurity Best Practices

## 👩‍💻 Author

**Anamika Chauhan**

Cyber Security Intern – Prodigy Infotech

GitHub: https://github.com/anamikachauhan07

## 📜 License

This project is created for educational purposes as part of the **Prodigy Infotech Cyber Security Internship (Task 03)**.
