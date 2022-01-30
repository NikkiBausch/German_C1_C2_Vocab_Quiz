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
    print("I created this quiz to collect and test my memory on new vocab words")
    print("that I learned while studying for the C2 OESD German Exam.")
    print("These words are suitable for German language learners at C1 or low C2 level.")
    print("There are 100 questions and the answers will be displayed at the end of the quiz.")
    print("You have 3 chances to answer the question correctly.")
    print("Type skip to move on to the next question.")
    print("umlauted vowels and the German character for ss are not recognized by Python")
    print("So you must use oe, ue, ae and ss where otherwise there would be characters from the German alphabet.")
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
   
print(f"Deine Gesamtpunktezahl ist {score} Punkte!\n\n")
print("Die richtigen Antworten sind:")
print_dictionary()

 