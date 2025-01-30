#! /bin/bash

import random

def main():

    money = 10

    while(money>0):
        choice = input("""
              Lottery is $2.
              You have $"""+str(money)+""".
              ------------------
              Press G to gamble
              Press Q to quit 
              """).upper()
        if choice == "G":
            money = money -2
            winnings = lottery()
            money  = money + winnings
        elif choice == "Q":
            break
    print("Game Over!")



    

def lottery():
    prize1 = (5, 10, 50, 100)
    prize2 = (200, 300, 500, 1000)
    prize3 = (2000, 5000, 10000, 20000)    

    lottery = []
    guess = []

    matches = 0

    amountOfNumbers = random.randint(5,10)

    for x in range(amountOfNumbers):
        lottery.append(random.randint(0,9))
               
    
    answerInput = False

    while(answerInput == False):
        answer = input("Enter your " + str(amountOfNumbers) + " numbers: ")
        if len(answer) == amountOfNumbers and answer.isdigit():
            answerInput = True
        else:
            print("ERROR! Enter " + str(amountOfNumbers) + " digits!")
    
    
    for i in answer:
        guess.append(int(i))
        
    
    for x in range(amountOfNumbers):
        if lottery[x] == guess[x]:
            matches = matches + 1


    print("Lottery numbers: " + str(lottery))
    print("Your numbers: " + str(guess))

    print("You got "+ str(matches) + " matches!")

    if matches <= 2:
        print("You didn't win anything!")
        winnings = 0
        return winnings
    elif matches <= 5:
        winnings = random.choice(prize1)
        print("You won $" + str(winnings) + "!")
        return winnings
    elif matches <= 8:
        winnings = random.choice(prize2)
        print("You won $" + str(winnings) + "!")
        return winnings
    elif matches <= 10:
        winnings = random.choice(prize3)
        print("You won $" + str(winnings) + "!")
        return winnings

       
    
if __name__ == "__main__":
    main()