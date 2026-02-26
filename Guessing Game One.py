def probability_calculator(lower, upper):
    """ This function calculates the probability of guessing a number correctly based on the current lower and upper bounds.
    It takes the lower and upper bounds as input and returns the probability as a percentage."""
    remaining = upper - lower + 1
    if remaining <= 0:
        return 0
    else:
        return (1/remaining) * 100

def transform_list_to_str(lst):
    """This function takes a list of items and transforms it into a string with the items separated by commas and 'and' before the last item.
    For example, if the input list is ['apple', 'banana', 'cherry'], the output will be 'apple, banana and cherry'."""     
    if len(lst) == 0:
        text = ""
    elif len(lst) == 1:
        text = str(lst[0])
    else:
        text = ", ".join(map(str,lst[:-1])) + " and " + str(lst[-1])
    return text
def guessing_game():
    """This is a simple number guessing game where the user has to guess a random number between 1 and 10. 
    The program generates a random number and prompts the user to enter their guess. 
    It provides feedback on whether the guess is too low, too high, or correct. 
    The game continues until the user guesses the number correctly."""
    import random
    # We import random to generate a random number between 1 and 10 and initialize the number of tries and a list to keep track of the numbers tried by the user.
    random_number = random.randint(1,10)
    lower = 1
    upper = 10
    tries = 0
    numbers_tried = []
    remaining_list = []
    print ('Guess the number between 1 and 10.')
    print ('Write "exit" to finish the game')
    
    # We use a while loop to continuously prompt the user for their guess until they guess correctly. 
    while True:

        # At the beginning of each iteration, we calculate and display the probability of guessing the number correctly based on the current lower and upper bounds.
        # We ask the user to input their guess and strip any leading or trailing whitespace. 
        # We also convert the input to lowercase to make it easier to check for the "exit" command.
        print(f'Right now your probability of guessing the number is about: {probability_calculator(lower, upper):.2f} %')
        user_number = input('Enter your guess: ').strip().lower()
        if user_number == 'exit':
            print('Game over', 'Bye!', sep='\n')
            break
        
        # We check if the input is a digit. If it is, we convert it to an integer and compare it to the random number.
        if user_number.isdigit():
            user_number = int(user_number)
            print(f'You guessed {user_number}')
            # We check if the user's guess is between 1 and 10. If it is, we check if they have already tried that number. 
            # If they haven't, we add it to the list of numbers tried and increment the number of tries. 
            # If they have already tried that number, we inform them and prompt them to try a different one.
            if 1 <= user_number <= 10:
                if user_number not in numbers_tried:
                    tries += 1
                    numbers_tried.append(user_number)
                    numbers_tried.sort()
                else:
                    print(f'You have already tried this number. Try a different one.')
                    continue 
                # We compare the user's guess to the random number and provide feedback accordingly.
                # If the guess is correct, we congratulate the user and break out of the loop.
                # If the guess is too low or too high, we inform the user and prompt them to try again.
                if user_number == random_number:
                    print(f'Congratulations! You guessed the number correctly in {tries} tries.', f'The number was {random_number}.', sep= '\n')
                    break
                elif user_number < random_number: 
                    lower = user_number + 1
                    print('Too low! Try again.')
                elif user_number > random_number:
                    upper = user_number - 1
                    print('Too high! Try again.')
                print(f'You have tried number {transform_list_to_str(numbers_tried)}' if len(numbers_tried) == 1 else f'You have tried numbers {transform_list_to_str(numbers_tried)}.')
            # If the user's guess is not between 1 and 10, we inform them that the input is invalid and prompt them to enter a valid number. 
            else:
                print('Invalid input. The number has to be between 1 and 10.')
                
        # If the input is not a digit, we inform the user that the input is invalid and prompt them to enter a valid number.
        else:
            print('Invalid input. The input must be a number between 1 and 10.')