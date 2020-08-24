"""
ex2.py
CE151 assignment 2
created by Thomas Harris 04/12/14
"""
import random

word = " "
fileName = input("Please supply name of input file: ")
try :
    gotIt = open(fileName)
except IOError as e :
    gotIt = None
    print("Failed to open", fileName)
if gotIt != None :
    mylist = [line.strip() for line in gotIt]
    word = random.choice(mylist)

    lives = 0
    while lives == 0:
        n = input("Pick your difficulty (Easy, Normal or Hard): ")
        if n == "Easy":
            lives = 12
        elif n == "Normal":
            lives = 8
        elif n == "Hard":
            lives = 5
        else: print("Invalid Input Try Again")
          
    guesses = ""
    while lives > 0:         
        failed = 0
        WORDCURRENT = ""
        for x in word:
            if x in guesses:    
                WORDCURRENT = WORDCURRENT + x    
            else:
                WORDCURRENT = WORDCURRENT +"*"     
                failed += 1
        print(WORDCURRENT)
        if failed == 0:        
            print("You won")  
            break              

        guess = input("Guess A Character (IN CAPITALS):") 
        guesses += guess                    

        if guess not in word:  
            lives = lives-1        
            print("The letter", guess, "does not occur in the word")
            print("You have", lives, "more lives")
        else:
            print("The letter", guess, "does occur in the word")
            print("You have", lives, "more lives")
        if lives == 0:           
            print("You Lose")
