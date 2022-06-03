import random

objects = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
options = [*objects.keys()]

while True:
    user_option = input('Choose one: (R)ock, (P)aper or (S)cissors >> ').upper()

    if user_option not in options:
        print('Error: Invalid option')
    else:
        cpu_option = random.choice(options)
        print(f"Player ({objects[user_option]}) : CPU ({objects[cpu_option]})")
        if user_option == cpu_option:
            print(f"You both chose {objects[user_option]}. It's a tie.")
        elif user_option == "R":
            if cpu_option == "S":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock. You lose.")
            break
        elif user_option == "P":
            if cpu_option == "R":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper. You lose.")
            break
        elif user_option == "S":
            if cpu_option == "P":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors. You lose.")
            break
