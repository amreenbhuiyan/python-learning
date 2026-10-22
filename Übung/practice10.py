questions = ("Liebt mich Fatihhan? ",
            "Sieht Fatihhan eine andere Frau an?",
            "Vermisst Fatihhan mich?",
            "Denkt Fatihhan an eine andere?")
options = (("A  JA","B NEIN","C VLLT","D RUN"),
          ("A  JA","B NEIN","C VLLT","D RUN"),
          ("A  JA","B NEIN","C VLLT","D RUN"),
          ("A  JA","B NEIN","C VLLT","D RUN"))

answer = ("A","C", "B", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess= input("guess answer:").upper()
    guesses.append(guess) #append zählt eine zahl dazu
    if guess == answer[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
    question_num += 1
    
print("answer :")
for all_answer in answer:
    print(all_answer, end=" ")
print()

print("guess :")
for guess in guesses:
    print(guess, end=" ")
    
    
    
    
        