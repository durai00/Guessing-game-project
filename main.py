import random
import time
import pygame

# initialize pygame mixer to play sounds
pygame.mixer.init()

# load sound effects for feedback
correct_sound = pygame.mixer.Sound("correct.mp3")
too_low = pygame.mixer.Sound("too_low.mp3")
too_high = pygame.mixer.Sound("too_high.mp3")

# function to generate a random number between 1 and 100
def generate_random_number():
    return random.randint(1, 100)

# function to display the high scores list
def display_high_scores(high_scores):
    print("\nHigh Scores:")
    # iterate over the scores and print them with their rank
    for index, score in enumerate(high_scores, start=1):
        print(f"{index}. {score}")

# function to get the user's guess
def get_user_guess(target):
    guess = input("Please enter your guess (1-100) or type 'quit' to exit: ")
    if guess.lower() == "quit":
        # if the user types "quit", return a special value to indicate this
        return "quit"

    guess = int(guess)
    if guess < target:
        # if the guess is too low, print a message and play a sound effect
        print("Too low!")
        too_low.play()
        return False
    elif guess > target:
        # if the guess is too high, print a message and play a sound effect
        print("Too high!")
        too_high.play()
        return False
    else:
        # if the guess is correct, print a message and play a sound effect
        print("Congratulations! You guessed the correct number.")
        correct_sound.play()
        return True

# function to update the high scores list
def update_high_scores(high_scores, num_of_guesses):
    # add the number of guesses to the list
    high_scores.append(num_of_guesses)
    # sort the list in ascending order
    high_scores.sort()
    # keep only the top 5 scores
    high_scores = high_scores[:5]
    return high_scores

# function to display a message to the player based on their performance
def display_message(scenario, num_of_guesses):
    if scenario == "first_try":
        # if the player guessed the number on the first try, display a special message
        print("Wow! You guessed the correct number on the first try!")
    elif scenario == "many_attempts":
        # if the player took multiple tries to guess the number, display how many attempts it took
        print(f"It took you {num_of_guesses} attempts to find the correct number.")
    elif scenario == "quit":
        # if the player quit the game, display a message saying so
        print("You quit the game before finding the correct number.")

# main function that runs the game
def main():
    high_scores = [] # initialize the high scores list
    while True:
        print("\nWelcome to the number guessing game!")
        target_number = generate_random_number() # generate a random target number
        num_of_guesses = 0 # initialize the number of guesses to 0
        is_correct = False # initialize the flag to indicate whether the player guessed correctly

        start_time = time.time() # start the timer
        while not is_correct:
            is_correct = get_user_guess(target_number) # get the player's guess
            if is_correct == "quit":
                # if the player quits, set a flag to indicate this and break out of the loop
                scenario = "quit"
                break

            num_of_guesses += 1  # increment the number of guesses
            end_time = time.time()

            if is_correct:
                # if the player guessed correctly, calculate the elapsed time and display a message based on their performance
                elapsed_time = end_time - start_time
                if num_of_guesses == 1:
                    scenario = "first_try"
                else:
                    scenario = "many_attempts"
                display_message(scenario, num_of_guesses)
                print(f"Time elapsed: {round(elapsed_time, 2)} seconds")
                # update the high scores list
                high_scores = update_high_scores(high_scores, num_of_guesses)
                # display the high scores list
                display_high_scores(high_scores)

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

    print("Thanks for playing the number guessing game!")

if __name__ == "__main__":
    main()
