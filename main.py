import random
import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the grid with headers and labels
def print_grid(grid, label):
    print(f"{label} Grid:")
    print("    0   1   2   3   4   5   6   7   8   9")
    print("- " * 10)
    for i in range(10):
        print(f"{i}|", end=" ")
        for j in range(10):
            print(grid[i][j], end=" ")
        print()

# Function to place ships on the grid
def place_ship(grid, length):
    while True:
        xco, yco = random.randint(0, 9), random.randint(0, 9)
        direction = random.choice(["right", "left", "up", "down"])
        ship_positions = []

        if direction == "right" and yco + length <= 10:
            ship_positions = [(xco, yco + i) for i in range(length)]
        elif direction == "left" and yco - length + 1 >= 0:
            ship_positions = [(xco, yco - i) for i in range(length)]
        elif direction == "down" and xco + length <= 10:
            ship_positions = [(xco + i, yco) for i in range(length)]
        elif direction == "up" and xco - length + 1 >= 0:
            ship_positions = [(xco - i, yco) for i in range(length)]

        if all(grid[x][y] == ' o ' for x, y in ship_positions):
            for x, y in ship_positions:
                grid[x][y] = ' # '
            break

# Function to take a shot
def take_shot(grid, x, y):
    if grid[x][y] == ' # ':
        grid[x][y] = ' X '
        return True
    else:
        grid[x][y] = ' - '
        return False

# Main game function
def play_battleship():
    grid_player = [[' o ' for _ in range(10)] for _ in range(10)]
    grid_computer = [[' o ' for _ in range(10)] for _ in range(10)]

    # Place ships for player and computer
    ship_sizes = [5, 4, 3, 3, 2]

    for size in ship_sizes:
        place_ship(grid_player, size)
        place_ship(grid_computer, size)

    while True:
        clear_screen()
        print_grid(grid_player, "Your")
        print("\n")
        print_grid(grid_computer, "Computer's")

        # Player's turn
        try:
            player_x = int(input("Enter X coordinate: "))
            player_y = int(input("Enter Y coordinate: "))
            if 0 <= player_x < 10 and 0 <= player_y < 10:
                player_hit = take_shot(grid_computer, player_x, player_y)
                if player_hit:
                    print("You hit a ship!")
                else:
                    print("Your shot missed.")
                input("Press Enter to continue...")

                # Check if player wins
                if all(cell != ' # ' for row in grid_computer for cell in row):
                    clear_screen()
                    print("Congratulations! You sank all of computer's ships. You win!")
                    break

                clear_screen()

                # Computer's turn
                computer_x = random.randint(0, 9)
                computer_y = random.randint(0, 9)
                computer_hit = take_shot(grid_player, computer_x, computer_y)
                print(f"Computer's shot: X = {computer_x}, Y = {computer_y}")
                if computer_hit:
                    print("Computer hit your ship!")
                else:
                    print("Computer's shot missed.")

                # Check if computer wins
                if all(cell != ' # ' for row in grid_player for cell in row):
                    clear_screen()
                    print("Sorry, all of your ships are destroyed. Computer wins!")
                    break

                input("Press Enter to continue...")

            else:
                print("Invalid coordinates! Please enter numbers between 0 and 9.")
        except ValueError:
            print("Invalid input! Please enter numerical coordinates.")

# Run the game
play_battleship()
