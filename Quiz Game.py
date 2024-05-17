def ask_question(question, correct_answer):
    incorrect_count = 0  # Initialize the counter for incorrect attempts
    score = 0  # Initiate the counter for correct answers

    while True:
        answer = input(question)

        if answer.lower() != correct_answer.lower():
            incorrect_count += 1  # Increment the incorrect counter
            if incorrect_count == 2:
                print("Incorrect! Are you slow or what?")
            if incorrect_count == 4:
                print("You must be dumb or something")
            if incorrect_count >= 5:
                break
            else:
                print("Incorrect. Try again.")
        else:
            score += 1
            print("Correct!")
            break

    return score

print("Welcome to my Quiz Game!")

playing = input("Do you want to Play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play")

# Ask questions and accumulate the score
score = ask_question("What is the color of the sky? A. red, B. green, C. blue, D. purple: ", "blue")
score += ask_question("What does CPU stand for? ", "central processing unit")
score += ask_question("What does GPU stand for? ", "graphics processing unit")
score += ask_question("How many letters are in the alphabet? ", "26")
score += ask_question("Where is the White House located? ", "Washington D.C")

print("You got " + str(score) + " questions correct out of 5!")
percentage_correct = (score / 5) * 100
print("That's " + "{:.2f}".format(percentage_correct) + "% questions correct!")

if score <= 4:
    print("Try again, Dumb Ass")
else:
    print("Good Job!")
