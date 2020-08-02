
no = 20     #the no to be guessed
j = 1   #initializing the no of guesses
while(j <= 3):
    i = int(input("Enter the guessing no\n"))

    if i > no:
        print("Your no is greater try with smaller no ")
    elif i < no:
        print("Your no is smaller try with bigger no")
    else:
        print("you have guessed the right no congratulations -_-")
        print("You solved this in", j, "attempt")
        break
    print(3 - j, "guesses left")
    j = j+1
if(j > 3):
    print("Game Over")
