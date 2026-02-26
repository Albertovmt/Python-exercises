{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "525d2089",
   "metadata": {},
   "outputs": [],
   "source": [
    "def probability_calculator(lower, upper):\n",
    "    \"\"\" This function calculates the probability of guessing a number correctly based on the current lower and upper bounds.\n",
    "    It takes the lower and upper bounds as input and returns the probability as a percentage.\"\"\"\n",
    "    remaining = upper - lower + 1\n",
    "    if remaining <= 0:\n",
    "        return 0\n",
    "    else:\n",
    "        return (1/remaining) * 100\n",
    "\n",
    "def transform_list_to_str(lst):\n",
    "    \"\"\"This function takes a list of items and transforms it into a string with the items separated by commas and 'and' before the last item.\n",
    "    For example, if the input list is ['apple', 'banana', 'cherry'], the output will be 'apple, banana and cherry'.\"\"\"     \n",
    "    if len(lst) == 0:\n",
    "        text = \"\"\n",
    "    elif len(lst) == 1:\n",
    "        text = str(lst[0])\n",
    "    else:\n",
    "        text = \", \".join(map(str,lst[:-1])) + \" and \" + str(lst[-1])\n",
    "    return text\n",
    "def guessing_game():\n",
    "    \"\"\"This is a simple number guessing game where the user has to guess a random number between 1 and 10. \n",
    "    The program generates a random number and prompts the user to enter their guess. \n",
    "    It provides feedback on whether the guess is too low, too high, or correct. \n",
    "    The game continues until the user guesses the number correctly.\"\"\"\n",
    "    import random\n",
    "    # We import random to generate a random number between 1 and 10 and initialize the number of tries and a list to keep track of the numbers tried by the user.\n",
    "    random_number = random.randint(1,10)\n",
    "    lower = 1\n",
    "    upper = 10\n",
    "    tries = 0\n",
    "    numbers_tried = []\n",
    "    remaining_list = []\n",
    "    print ('Guess the number between 1 and 10.')\n",
    "    print ('Write \"exit\" to finish the game')\n",
    "    \n",
    "    # We use a while loop to continuously prompt the user for their guess until they guess correctly. \n",
    "    while True:\n",
    "\n",
    "        # At the beginning of each iteration, we calculate and display the probability of guessing the number correctly based on the current lower and upper bounds.\n",
    "        # We ask the user to input their guess and strip any leading or trailing whitespace. \n",
    "        # We also convert the input to lowercase to make it easier to check for the \"exit\" command.\n",
    "        print(f'Right now your probability of guessing the number is about: {probability_calculator(lower, upper):.2f} %')\n",
    "        user_number = input('Enter your guess: ').strip().lower()\n",
    "        if user_number == 'exit':\n",
    "            print('Game over', 'Bye!', sep='\\n')\n",
    "            break\n",
    "        \n",
    "        # We check if the input is a digit. If it is, we convert it to an integer and compare it to the random number.\n",
    "        if user_number.isdigit():\n",
    "            user_number = int(user_number)\n",
    "            print(f'You guessed {user_number}')\n",
    "            # We check if the user's guess is between 1 and 10. If it is, we check if they have already tried that number. \n",
    "            # If they haven't, we add it to the list of numbers tried and increment the number of tries. \n",
    "            # If they have already tried that number, we inform them and prompt them to try a different one.\n",
    "            if 1 <= user_number <= 10:\n",
    "                if user_number not in numbers_tried:\n",
    "                    tries += 1\n",
    "                    numbers_tried.append(user_number)\n",
    "                    numbers_tried.sort()\n",
    "                else:\n",
    "                    print(f'You have already tried this number. Try a different one.')\n",
    "                    continue \n",
    "                # We compare the user's guess to the random number and provide feedback accordingly.\n",
    "                # If the guess is correct, we congratulate the user and break out of the loop.\n",
    "                # If the guess is too low or too high, we inform the user and prompt them to try again.\n",
    "                if user_number == random_number:\n",
    "                    print(f'Congratulations! You guessed the number correctly in {tries} tries.', f'The number was {random_number}.', sep= '\\n')\n",
    "                    break\n",
    "                elif user_number < random_number: \n",
    "                    lower = user_number + 1\n",
    "                    print('Too low! Try again.')\n",
    "                elif user_number > random_number:\n",
    "                    upper = user_number - 1\n",
    "                    print('Too high! Try again.')\n",
    "                print(f'You have tried number {transform_list_to_str(numbers_tried)}' if len(numbers_tried) == 1 else f'You have tried numbers {transform_list_to_str(numbers_tried)}.')\n",
    "            # If the user's guess is not between 1 and 10, we inform them that the input is invalid and prompt them to enter a valid number. \n",
    "            else:\n",
    "                print('Invalid input. The number has to be between 1 and 10.')\n",
    "                \n",
    "        # If the input is not a digit, we inform the user that the input is invalid and prompt them to enter a valid number.\n",
    "        else:\n",
    "            print('Invalid input. The input must be a number between 1 and 10.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3415b005",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Guess the number between 1 and 10.\n",
      "Write \"exit\" to finish the game\n",
      "Right now your probability to guess the number is about: 10.00 %\n",
      "you guessed 5\n",
      "Congratulations! You guessed the number correctly in 1 tries.\n",
      "The number was 5.\n"
     ]
    }
   ],
   "source": [
    "guessing_game()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7d41990",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv-bootcamp",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
