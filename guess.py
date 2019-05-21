import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0
name = input("May I ask your name? ")

with open("score_list.txt", "r") as score_file:  #abrimos el archivo .txt para guardar en el la lista de resultados
    score_list = json.loads(score_file.read())

sorted_list = sorted(score_list, key=lambda k:k["attempts"])[:3]  #creamos una nueva lista ordenada que solo contenga el resulado de los 3 mejores intentos
print("Top scores: ")
for score_dict in sorted_list:  #bucle que recorre la lista ordenada y muestra por pantalla los valores de cada una de las claves almacenadas
    print(str(score_dict["attempts"]) + " Attempts, Date: " + str(score_dict.get("date")) + " Name:", str(score_dict.get("name")),
    " The secret number was:", str(score_dict.get("secret number")), " Missed numbers: " + str(score_dict.get("wrong_guesses")))

wrong_guess = []  #creamos una lista nueva para guardar los resultados erroneos

while True:  #bucle que comprueba si hemos acertado el numero o no
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1
    if guess == secret:
        fecha = datetime.datetime.now() #guardams la fecha actual en la variable fecha
        score_list.append({"attempts": attempts, "date": str(fecha.ctime()), "name": name, "secret number": secret, "wrong_guesses": wrong_guess}) #añadimos un diccionario dentro de nuestra lista
        with open("score_list.txt", "w") as score_file: #abrimos el archivo con nuestra lista en modo escritura
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        wrong_guess.append(guess)  #añadimos el numero que no es el correcto a la lista wrong_guess
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        wrong_guess.append(guess)  #añadimos el numero que no es el correcto a la lista wrong_guess

