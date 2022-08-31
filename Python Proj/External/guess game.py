def runagain():
    user = input("Do u want to run again? y/n : ")
    if (user == "y"):
        guess()
    elif (user == "n"):
        print("Bye Bye Thankyou ")


def guess():
    n = 903
    number_of_guesses = 1
    print("Number of guesses is limited to only 9 times: ")
    while number_of_guesses <= 9:
        guess_number = int(input("Guess the number :\n"))
        if guess_number < 903:
            print("you enter less number please input greater number.\n")
        elif guess_number > 903:
            print("you enter greater number please input smaller number.\n ")
        else:
            print("you won\n")
            print(number_of_guesses, "no.of guesses he took to finish.")
            runagain()
            break
        print(9 - number_of_guesses, "no. of guesses left")
        number_of_guesses = number_of_guesses + 1

    if number_of_guesses > 9:
        print("Game Over")

guess()