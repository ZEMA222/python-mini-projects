import random
import string

print("Hello i am your password generator i can help you to generate any password: ")

Length = None

while True:
    user_input = input("Enter an integer (or type 'exit' to quit): ").strip()

    if user_input.lower() == "exit":
        print("Goodbye!")
        break 

    try:
        Length = int(user_input)
        print(f"✔ Successfully captured length: {Length}\n")
        print("Generating password........")
        
        all_characters = string.ascii_letters + string.digits + string.punctuation
        
        password_list = random.choices(all_characters, k=Length)
        
        generated_password = "".join(password_list)
        
        print(f"🔒 Your generated password is: {generated_password}\n")
        
    except ValueError:
        print("❌ Invalid input! Please enter a valid whole number or type 'exit'.\n")