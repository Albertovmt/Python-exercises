# Write a program that generates two lists of random numbers between 1 and 20. Each list should have a random length between 15 and 20. 
# The program should then identify the numbers that are common to both lists and separate them into two new lists: one for even numbers and one for odd numbers. 
# Finally, the program should print the two new lists of common numbers, sorted in ascending order.

import random
list_one = [random.randint(1,20) for _ in range(random.randint(15,20))]
list_two =[random.randint(1,20) for _ in range(random.randint(15,20))]

list_common_one_two_even = []
list_common_one_two_odd = []

for number in list_one:
    if number in list_two and number not in list_common_one_two_even and number not in list_common_one_two_odd:
        if number % 2 == 0:
            list_common_one_two_even.append(number)
        else:
            list_common_one_two_odd.append(number)

list_common_one_two_even.sort()
list_common_one_two_odd.sort()

print(f'Even numbers common to both lists: {list_common_one_two_even}')
print(f'Odd numbers common to both lists: {list_common_one_two_odd}')