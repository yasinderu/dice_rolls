import random

def roll_dice(amount: int = 1) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for _ in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main():
    while True:
        try:
            user_input: str = input("How many dice would you like to roll? ")
            
            if user_input.lower() == "exit":
                print("Thanks for playing!")
                break

            dice = roll_dice(int(user_input))
            print(*dice, sep=', ')
            print(f"Total dice : {sum(dice)}")
            
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()