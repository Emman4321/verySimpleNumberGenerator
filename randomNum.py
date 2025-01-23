#random num generator

import random

def rand():
    print("Welcome to my random number generator!")

    min_num = int(input("Enter the minimum number: "))
    max_num = int(input("Enter the maximum number: "))   

    rand_num = random.randint(min_num, max_num)
    print("Your random number is: ", rand_num)
    
rand()
