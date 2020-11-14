import random
import time


print("\nBine ai venit la spanzuratoarea\n")
nume = input("Introdu numele tau: ")
print("Salut " + nume, "Noroc! ")
time.sleep(2)
print("Jocul incepe! \nSajucam")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ("Paine", "Masina", "Mobilier", "Alimente", "Sunete", "Incaltamine", "Pian")
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("Vrei sa mai joci? y = Yes, n = No \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Vrei sa mai joci odata? y = yes, n =no \n")
        if play_game == "y":
            main()
        elif play_game == "n":
            print("Iti multumim ca ai jucat! ")
            exit()
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("Acesta este cuvantul: " + display + "Introdu litera: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Litera invalida, mai incearca\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index +1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Incearca alta litera.\n")

    else:
        count = 1
        if count == 1:
            time.sleep(1)
            print("   ------ \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__ \n")
            print("Raspuns gresit. " + str(limit - count) + "Ghiceste literele ramase\n")
        elif count == 2:
            time.sleep(1)
            print("   ------ \n"
                  "  |      | \n"
                  "  |      |\n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__ \n")
            print("Raspuns gresit." + str(limit - count) + "Ghiceste literele ramase\n")
        elif count == 3:
            time.sleep(1)
            print("   ------ \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__ \n")
            print("Raspuns gresit. " + str(limit - count) + "Ghiceste literele ramase\n")
        elif count == 4:
            time.sleep(1)
            print("   ------ \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     O  \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__ \n")
            print("Raspuns gresit. " + str(limit - count) + "Ghiceste literele ramase\n")
        elif count == 5:
            time.sleep(1)
            print("   ------ \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     O  \n"
                  "  |    /|\   \n"
                  "  |    / \  \n"
                  "__|__ \n")
            print("Raspuns gresit, esti spanzurat!!!\n")
            print("Cuvantul era:", already_guessed, word)
            play_loop()
        if word == "_" *length:
            print("Felicitari! Ai ghicit cuvantul")
            play_loop()
        elif count != limit:
            hangman()
main()
hangman()
















