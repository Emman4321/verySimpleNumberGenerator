#random num generator

import random

def rand(min_num, max_num):
    
    return random.randint(min_num, max_num)

def main():
    print("Welcome to my random number generator!")
    
    try:
        min_num = int(input("Enter the minimum number: "))
        max_num = int(input("Enter the maximum number: "))
    
        if min_num > max_num:
            print("Error: Minimum number must be less than or equal to the max number")
        else:
            rand_num = rand(min_num, max_num)
            print("Your random number is: ", rand_num)
    
    except ValueError:
        print("Invalid input! Please enter valid integers.")


    
if __name__ == "__main__":
    main()
