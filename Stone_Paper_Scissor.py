import random as r

valid_moves = ['Stone', 'Paper', 'Scissor']
Score = 0
comp = 0
z = 'Yes'
while (z.strip().lower() in 'yes') :
    print('''MENU
1.)Stone
2.)Paper
3.)Scissor
''')

    a = input ("Your's turn- ").strip().capitalize()
    b = valid_moves[r.randint(0,2)]

    if a not in valid_moves :
       print("!!!Wrong Input!!!\nPlease Try Again...")

    elif (a == b):
        print("It's a Draw!")

    elif ((a == "Stone" and b == "Paper") or (b == "Stone" and a == "Scissor") or (a == "Paper" and b == "Scissor")):
        print("Computer wins")
        comp += 1

    else :
        print("You win")
        Score += 1 

    print(f'''Your Score = {Score} \t Bot Score = {comp}''')

    z = input("Do you want to play again? (Yes/No): ")

print("Thank You for playing")