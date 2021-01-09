import random
import time

#This is a program that will flip a coin a thousand times and return and print the results

flips = 0
heads = 0
tails = 0
numberOfFlips = 1000

print(" Now I shall flip this coin a " + str(numberOfFlips) + " times!")
input("press enter to continue\n")

def coinFlipper(repeats):
    global flips, heads, tails
    while flips < numberOfFlips:
        if random.randint(0, 1) == 1:
            heads = heads + 1

        else:
            tails = tails + 1

        flips = flips + 1

        if flips == 100:
            print("900 coin flips remaining!")
            time.sleep(.5)

        elif flips == 500:
            print("500 coin flips remaining!")
            time.sleep(.5)

        elif flips == 900:
              print("100 coin flips remaining!")
              time.sleep(.5)

coinFlipper(flips)
print("""\nThe number of heads was... """ + str(heads) + "!\nWas your guess close to the outcome?" )
