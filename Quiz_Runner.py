from Question_Bank import Quiz_Bank

def check_ans(question, ans, attempts, score):
    if Quiz_Bank[question]['answer'].lower()==ans.lower():
        print(f"Richtige Antwort! \nDu hast jetzt {score + 1} Punkte gewonnen!")
        return True
    else:
        print(f"Falsche Antwort! \nDu hast noch {attempts - 1} Chancen. ")
        return False 

def print_dictionary():
    for question_id, question_answer in Quiz_Bank.items():
        for key in question_answer:
            print(key + ':', question_answer[key])

def intro_message():
    print("Welcome Message with explanation of what this is")
    print("Welcome message")
    print("Explanation about the testing level")
    print("More explanation about the testing level")
    print("Directions about Skipping")
    input("Press any key to start the quiz.")
    return True

intro = intro_message()    
while True:
    score=0 
    for question in Quiz_Bank:
        attempts = 3 
        while attempts <= 3:
            print(Quiz_Bank[question]['question']) 
            answer = input("Antwort eingeben: ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1
     

    break 
   
print(f"final score is {score}!\n\n")
print("Want to know the correct answers? See below.")
print_dictionary()
print("Thanks for playing!")
 