import random

min_number = 1
max_number = 10

random_number = random.randint(min_number, max_number)

def start_game():
    print("Hello! Welcome to the number guessing game. Can you guess a number between 1 and 10?"  )
    user_guess = input(">  ")
    number_of_guesses = 5
    while number_of_guesses >= 1:
        try:
            user_guess = int(user_guess)
            if user_guess > 10 or user_guess < 1:
                raise ValueError
        except ValueError:
            print("That's not a valid guess, try again!")
            user_guess = input(">  ")
            continue
        else:
            if user_guess > random_number:
                number_of_guesses -= 1
                print("That number is too high.  Try again! You have " + str(number_of_guesses) + " guesses left")
                user_guess = input(">  ")
                continue
            elif user_guess < random_number:
                number_of_guesses -= 1
                print("That number is too low. Try again! You have " + str(number_of_guesses) + " guesses left")
                user_guess = input(">  ")
                continue
            else:
                print("You guessed correctly! Congratulations!")      
                play_again = input("Would you like to play again Y/N?  ")
                if play_again.lower == "n":
                    print("Game Over. Thanks for playing!")
                    break
                else:play_again.lower == "y"
                start_game()
    else:
        print("Sorry, you are out of guesses. Please try again!")
        play_again = input("Would you like to play again Y/N?  ")
        if play_again.lower == "n":
            print("Game Over. Thanks for playing!")
            break
        else: play_again.lower == "y"    
        start_game()    
                                

    
start_game()    
              
#the application works perfectly until it is suppose to end or restart
    # I need to get the count to end at 0 and print the play again prompt
    # I need to make sure the game restarts on a "Y" after play_again prompt
    #
    
    
        
    