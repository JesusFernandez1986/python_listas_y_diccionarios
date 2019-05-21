import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0
name = input("May I ask your name? ")

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

print("Top scores: ")

for score_dict in score_list:
   print(str(score_dict["attempts"]) + " Attempts, Date: " + str(score_dict.get("date")) + " Name:", str(score_dict.get("name")),
   " The secret number was:", str(score_dict.get("secret number")), " Missed numbers: " + str(score_dict.get("wrong_guesses")))


wrong_guess = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1
    if guess == secret:
        fecha = datetime.datetime.now()
        score_list.append({"attempts": attempts, "date": str(fecha.ctime()), "name": name, "secret number": secret, "wrong_guesses": wrong_guess})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        wrong_guess.append(guess)
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        wrong_guess.append(guess)




