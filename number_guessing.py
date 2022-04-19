import random

min_number = 1
max_number = 100

random_number = random.randint(min_number, max_number)

def start_game():
    print("Hello! Welcome to the number guessing game. Can you guess a number between 1 and 100?"  )
    user_guess = (input(">  "))
    number_of_guesses = 5
    while number_of_guesses != 0:
        try:
            user_guess = int(user_guess)
            if user_guess > 100 or user_guess < 1:
                raise ValueError
        except ValueError:
            print("That's not a number, try again!")
        else:
            if user_guess > random_number:
                number_of_guesses -= 1
                print("That number is too high.  Try again! You have " + str(number_of_guesses) + " guesses left")
                continue
            elif user_guess < random_number:
                number_of_guesses -= 1
                print("That number is too low. Try again! You have " + str(number_of_guesses) + " guesses left")
                continue
            elif number_of_guesses == 0:
                print("Sorry, you are out of guesses. Please try again!")
                play_again = input("Would you like to play again Y/N?  ")
                break
            else:
                print("You guessed correctly! Congratulations!")      
                play_again
                while True:
                    if play_again.upper == "Y":
                        start_game()
                    elif play_again.upper == "N":
                        print("Game Over. Thanks for playing!")
                        break

    
start_game()    
              
        
    