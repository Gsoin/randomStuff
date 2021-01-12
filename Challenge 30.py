def guessgame():
    guess = int(input("Guess a number between 1 and 10: "))
    import random
    
    num = random.randint(0,10)
    
    if (guess == num):
         print("Congrats! You have won!")
    elif (guess < num):
        print("You guessed lower!")

    elif (num < guess):
        print("You have guessed higher!")

guessgame()
     
     
