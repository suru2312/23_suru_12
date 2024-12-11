import random

print("-----Welcome to the Number Guessing Game-----")
try:
    lower_bound = int(input("Enter Lower Bound : "))
    upper_bound = int(input("Enter Upper Bound : "))

    if lower_bound > 0 and upper_bound > 0:
        if lower_bound < upper_bound:
            random_int = random.randint(lower_bound,upper_bound)
            print("You have 7 chances for Guessing the Integer...")
            print()
            attempts = 0
            while True:
                try:
                    guess = int(input("Guess a Number : "))
                    attempts += 1
                    if guess == random_int:
                        print(f"Congrats you guessed it in {attempts} attempts.")
                        print("Thankyou for Playing the Game.......")
                        break
                    elif guess < random_int:
                        print("Your Guess is too Small.")
                    elif guess > random_int:
                        print("Your Guess is too High.")
                    
                    if attempts == 7:
                        print("You have Run out of Chances.")
                        print(f"Actual Number is : {random_int}")
                        print("Thankyou for Playing the Game.......")
                        print()
                        break
                except:
                    print("Enter a Valid Number.")
                    break
        else:
            print("Lower Bound cannot be smaller or equal to the Upper Bound.")
except:
    print("Enter Positive Integers Only.")