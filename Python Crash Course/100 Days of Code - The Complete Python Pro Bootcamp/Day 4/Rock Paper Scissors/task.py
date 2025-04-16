import random

def rps_game():

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    # Refactor using and, or, not clause
    # todo: user_choice== 0 and cpu_choice == 2 : You win
    # todo: cpu_choice > user_choice : You lose
    # todo: cpu_choice == user_choice : It's a draw

    rps_ascii_list = [rock, paper, scissors]
    rps_cpu_choice = random.choice(rps_ascii_list)
    user_input = input("What do you choose? 0 for Rock, 1 for Paper, and 2 for Scissors: \n")

    if user_input == "0":
        print(rps_ascii_list[0])
        if rps_cpu_choice == rps_ascii_list[0]:
            print(f" \n Computer chose: {rps_cpu_choice} \n. It's a tie.")
        elif rps_cpu_choice == rps_ascii_list[1]:
            print(f" \n Computer chose: {rps_cpu_choice} \n. You lose.")
        elif rps_cpu_choice == rps_ascii_list[2]:
            print(f" \n Computer chose: \n {rps_cpu_choice} \n. You win.")
        else:
            print("Invalid choice.")

    if user_input == "1":
        print(rps_ascii_list[1])
        print(rps_cpu_choice)
        if rps_cpu_choice == rps_ascii_list[0]:
            print(f"  Computer chose: {rps_cpu_choice}. \n You win.")
        elif rps_cpu_choice == rps_ascii_list[1]:
            print(f"  Computer chose: {rps_cpu_choice}. \n It's a tie.")
        elif rps_cpu_choice == rps_ascii_list[2]:
            print(f"  Computer chose: {rps_cpu_choice}. \n You lose.")
        else:
            print("Invalid choice.")

    if user_input == "2":
        print(rps_ascii_list[2])
        print(rps_cpu_choice)
        if rps_cpu_choice == 0:
            print(f"  Computer chose: \n {rps_cpu_choice}. \n You lose.")
        elif rps_cpu_choice == 1:
            print(f"  Computer chose: \n {rps_cpu_choice}. \n You win.")
        elif rps_cpu_choice == 2:
            print(f"  Computer chose: \n {rps_cpu_choice}. \n It's a tie.")
        else:
            print("Invalid choice.")

rps_game()
