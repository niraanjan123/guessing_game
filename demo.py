from random import randint

...
#making a random number with randint algorithm
...


print("AUTHOR  : NIRANJAN REDDY  ")
value=randint(1,1000)
print("The computer assisgned a value for you between range 1 to 1000")
count=0

guess=None
while guess!=value:
    guess=int(input("enter your guessing number : "))
    if guess>value:
        print("the number is lower than ",guess)
    elif guess<value:
        print("the number is greater than ",guess)
    count=count+1

print("congratulation...... you won the game after {} atempts".format(count))
print("if you want to play it ,go back and press the link one more time ")
