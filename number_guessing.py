import random
import statistics
from statistics import mean, median, mode


min_number = 1
max_number = 10


def start_game():
    print("Can you guess a number between 1 and 10?")
    number_of_guesses = 5
    score = 0
    score_list = []
    random_number = random.randint(min_number, max_number)
    while number_of_guesses > 0:
        user_guess = input(">  ")
        try:
            user_guess = int(user_guess)
            if user_guess > max_number or user_guess < min_number:
                raise ValueError
        except ValueError:
            print("That's not a valid guess, try again!")
            continue
        else:
            if user_guess > random_number:
                number_of_guesses -= 1
                score += 1
                print("That number is too high.  Try again! You have " + str(number_of_guesses) + " guesses left")
                
            elif user_guess < random_number:
                number_of_guesses -= 1
                score += 1
                print("That number is too low. Try again! You have " + str(number_of_guesses) + " guesses left")
            else:
                print("You guessed correctly! Congratulations! You had " + str(number_of_guesses) + " guesses left")      
                play_again = ""
                while play_again.lower() != "y" and play_again.lower() != "n":
                    play_again = input("Would you like to play again Y/N?  ")
                if play_again.lower() == "n":
                    print("Game Over. Thanks for playing!")
                    score_list.append(score)
                    score_list = sorted(score_list)
                    mean_score = mean(score_list)
                    print(f"Mean Score: {mean_score}")
                    median_score = median(score_list)
                    print(f"Median Score: {median_score}")
                    mode_score = mode(score_list)
                    print(f"Mode Score: {mode_score}")
                    exit()
                else:
                    start_game()  
    else:
        print("Sorry, you are out of guesses. Please try again!")
        play_again = ""
        while play_again.lower() != "y" and play_again.lower() != "n":
            play_again = input("Would you like to play again Y/N?  ")
        if play_again.lower() == "n":
            print("Game Over. Thanks for playing!")
            score_list.append(score)
            score_list = sorted(score_list)
            mean_score = mean(score_list)
            print(f"Mean Score: {mean_score}")
            median_score = median(score_list)
            print(f"Median Score: {median_score}")
            mode_score = mode(score_list)
            print(f"Mode Score: {mode_score}")
        else:
            start_game()   
                       

print("Hello! Welcome to the number guessing game.")    
start_game()    
