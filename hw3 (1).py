import os  # used to check if the temporary file exists or not
import math  # needed for pi constant and pow
import time  # needed to report the execution time of the first problem
import tempfile  # needed for crating temporary files


#   problem 1
def play_fizz_buzz():
    """"
    This function "plays" the FizzBuzz game for the numbers between 1 and 100 and,
     at the end, it displays the execution time of the game
    """

    start_time = time.time()  # get the time before "playing" the game
    # generate the numbers from 1 to 100 inclusive, I am using a for statement and the range function
    # here is where I found additional info about the range function https://www.w3schools.com/python/ref_func_range.asp

    for num in range(1, 101):  # I have put 101 because the range function does not include the last param
        if num % 5 == 0 and num % 3 == 0:  # if the number is divisible by 5 and 3
            print("FizzBuzz")
        elif num % 5 == 0:  # if the number is divisible by 5
            print("Buzz")
        elif num % 3 == 0:  # if the number is divisible by 3
            print("Fizz")
        else:
            print(num)

    end_time = time.time()  # get the time after "playing" the game
    # compute the execution time in seconds
    exec_time = end_time - start_time
    print('The execution time of the FizzBuzz game is ', exec_time, ' seconds')


