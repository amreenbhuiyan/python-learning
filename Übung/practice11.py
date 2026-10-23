# def steht für define
def new_game():

    guesses = []
    correct_guesses = 0
    quesstion_num = 1

    for key in questions:
        print(key)
        for i in options[quesstion_num - 1]:
            print(i)

        guess = input("guess answer:").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        quesstion_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("incorrect")
        return 0


def display_score(correct_guesses, guesses):
    print("results")
    print("answer: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


def play_again():
    response = input("Do you want to play agaian? (y/n):").upper()

    if response == "Y":
        return True
    else:
        return False


questions = {
    "Liebt mich Fatihhan? ": "A",
    "Sieht Fatihhan eine andere Frau an?": "B",
    "Vermisst Fatihhan mich?": "A",
    "Denkt Fatihhan an eine andere?": "B",
}

options = [
    ["A  JA", "B NEIN", "C VLLT", "D RUN"],
    ["A  JA", "B NEIN", "C VLLT", "D RUN"],
    ["A  JA", "B NEIN", "C VLLT", "D RUN"],
    ["A  JA", "B NEIN", "C VLLT", "D RUN"],
]

new_game()

while play_again():
    new_game()

print("Byeeeee")

