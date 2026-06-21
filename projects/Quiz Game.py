Questions = {
    "Question 1" : ["What is 2+2: " , 4],
    "Question 2" : ["What is 4+4: " , 8],
    "Question 3" : ["What is 5+5: " , 10],
    "Question 4" : ["What is 6+6: " , 12],
    "Question 5" : ["What is 7+7: " , 14]
}

score = 0
answer = None 

for k, v in Questions.items():
    print(f"\n {k}")
    

    while True:
        try:
            
            answer = int(input(v[0])) 
            break 
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")

            

    if answer == v[1]:
        print("✔ Correct Answer!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {v[1]}")

print(f"\nYour Final Score is: {score}/{len(Questions)}")