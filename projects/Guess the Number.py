import random

secret_number = random.randint(0, 10)

print("Eeny, meeny, miny, moe... can you guess the number bro? (0 to 10)")

guessed = int(input("Your Guess: "))

while guessed != secret_number:
    print("OOPS!!... Wrong Answer")
    
    if guessed < secret_number:
        print("Hint: Try a HIGHER number! 📈")
    
    elif guessed > secret_number:
        print("Hint: Try a LOWER number! 📉")
        
    guessed = int(input("Try again: "))

print("🎉 WIN!!! You got it!")