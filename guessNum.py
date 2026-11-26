import random
# Random number
num = random.randint(1, 100)
print("==== Guessing Number Game ====")
print("Computer gave a number from 1 to 100.")
print("You have maximum 5 times to guess this number.")

# Guess the number
tmp = 0
for i in range(0,5):
   
    print(f"Try {i + 1}: " , end=" ")
    yourNum = int(input())
    if yourNum == num:
        print("Congratulation! You are correct.")
        break
    elif yourNum > num:
        print("Find a smaller number!")
    else:
        print("Find a larger number!")
    tmp = i

if tmp == 4:
    print("You used 5 times to guess.")

