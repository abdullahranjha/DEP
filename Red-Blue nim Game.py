import random

def human_move(piles):
    while True:
        try:
            red_choice = int(input(f"Red marbles left ({piles[0]}): How many red marbles do you want to remove? "))
            blue_choice = int(input(f"Blue marbles left ({piles[1]}): How many blue marbles do you want to remove? "))
            if red_choice >= 0 and blue_choice >= 0 and red_choice + blue_choice > 0:
                return red_choice, blue_choice
            else:
                print("Invalid input. Please choose at least one marble.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")



def computer_move(piles, version):
    if version == "standard":
        
        if piles[0] > piles[1]:
            return 2, 0  
        else:
            return 0, 2  
    else:
        
        if piles[0] > piles[1]:
            return 1, 1  
        else:
            return 1, 1  


def evaluate_state(piles):
    return 2 * piles[0] + 3 * piles[1]


def main():
    num_red = int(input("Enter the number of red marbles: "))
    num_blue = int(input("Enter the number of blue marbles: "))
    version = input("Choose game version (standard/misere): ").lower()
    first_player = input("Choose starting player (computer/human): ").lower()

    piles = [num_red, num_blue]
    current_player = first_player

    while True:
        print(f"\nCurrent state: {piles[0]} red marbles, {piles[1]} blue marbles")
        if current_player == "human":
            red_choice, blue_choice = human_move(piles)
        else:
            red_choice, blue_choice = computer_move(piles, version)

        piles[0] -= red_choice
        piles[1] -= blue_choice
        current_player = "computer" if current_player == "human" else "human"

        if piles[0] == 0 or piles[1] == 0:
            break

    final_score = evaluate_state(piles)
    print(f"\nGame over! Final score: {final_score} points.")

if __name__ == "__main__":
    main()
