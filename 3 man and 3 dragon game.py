import time

# Helper function to print the current state of the game (simplified)
def print_state(left_people, left_dragons, right_people, right_dragons, boat_position):
    """Display the current state of the crossing with characters."""
    person_char = "👨"
    dragon_char = "🐉"
    boat_char = "🚤"
    
    # Left side and right side visual representation
    left_side = person_char * left_people + dragon_char * left_dragons
    right_side = person_char * right_people + dragon_char * right_dragons
    
    # Boat position: 0 = left, 1 = right
    if boat_position == 0:
        left_side = boat_char + left_side
    else:
        right_side = boat_char + right_side
    
    # Printing the visual representation without the "Left Point" and "Right Point" text
    print(f"\n{left_side}   ~~~~  {right_side}")
    print("-" * 40)

# Function to check if the current state is valid
def is_valid_state(left_people, left_dragons, right_people, right_dragons):
    """Check if the current state is valid based on the riddle rules."""
    # No side should have more dragons than people unless there are no people on that side.
    if (left_people > 0 and left_dragons > left_people) or (right_people > 0 and right_dragons > right_people):
        return False
    return True

# Function to handle the game logic
def crossing_game():
    print("Welcome to the '3 People and 3 Dragons Crossing the River' game!")
    time.sleep(1)
    print("You have three people (👨) and three dragons (🐉) who need to cross the river.")
    print("The boat can carry one or two creatures at a time.")
    print("At no point should the number of dragons outnumber the number of people on either side.")
    print("Make moves like 'p', 'd', 'p p', 'd d', or 'p d'.")
    time.sleep(1)
    
    # Initial state: 3 people and 3 dragons on the left side
    left_people = 3
    left_dragons = 3
    right_people = 0
    right_dragons = 0
    boat_position = 0  # 0: left, 1: right
    
    # Main game loop
    while left_people > 0 or left_dragons > 0:  # Game continues until everything is on the right side
        print_state(left_people, left_dragons, right_people, right_dragons, boat_position)
        
        # Get user input for the next move
        move = input("Which creatures would you like to send across the river? (e.g., 'p p'): ").strip().lower()
        
        # Split the input into parts
        move_parts = move.split()
        
        # Allow single or double moves
        if len(move_parts) == 1:
            if move_parts[0] in ['p', 'd']:
                move_parts = [move_parts[0]]
            else:
                print("Invalid move! Use 'p', 'd', 'p p', 'd d', or 'p d'.")
                continue
        elif len(move_parts) == 2:
            if not all(part in ['p', 'd'] for part in move_parts):
                print("Invalid move! Use 'p', 'd', 'p p', 'd d', or 'p d'.")
                continue
        else:
            print("Invalid move! Use 'p', 'd', 'p p', 'd d', or 'p d'.")
            continue
        
        # Determine the number of people and dragons to move
        move_people = move_parts.count('p')
        move_dragons = move_parts.count('d')
        
        # Validate the number of creatures being moved
        if move_people + move_dragons > 2 or move_people + move_dragons < 1:
            print("Invalid move! You can only move one or two creatures.")
            continue
        
        # Variables to store previous state for rollback if needed
        prev_left_people = left_people
        prev_left_dragons = left_dragons
        prev_right_people = right_people
        prev_right_dragons = right_dragons
        prev_boat_position = boat_position
        
        # Move creatures based on boat position
        if boat_position == 0:  # Boat on the left
            if left_people >= move_people and left_dragons >= move_dragons:
                left_people -= move_people
                left_dragons -= move_dragons
                right_people += move_people
                right_dragons += move_dragons
                boat_position = 1  # Move boat to the right
            else:
                print("Not enough creatures on the left side to make that move.")
                continue
        else:  # Boat on the right
            if right_people >= move_people and right_dragons >= move_dragons:
                right_people -= move_people
                right_dragons -= move_dragons
                left_people += move_people
                left_dragons += move_dragons
                boat_position = 0  # Move boat to the left
            else:
                print("Not enough creatures on the right side to make that move.")
                continue
        
        # Check if the new state is valid
        if not is_valid_state(left_people, left_dragons, right_people, right_dragons):
            print("Invalid move! Dragons outnumber people on one side.")
            # Revert to previous state
            left_people = prev_left_people
            left_dragons = prev_left_dragons
            right_people = prev_right_people
            right_dragons = prev_right_dragons
            boat_position = prev_boat_position
            continue
        
        # Provide feedback based on the move
        if boat_position == 1:
            # Moved from left to right
            if move_people == 2 and move_dragons == 0:
                print("Two people crossed to the right side!")
            elif move_people == 0 and move_dragons == 2:
                print("Two dragons crossed to the right side!")
            elif move_people == 1 and move_dragons == 1:
                print("One person and one dragon crossed to the right side!")
        else:
            # Moved from right to left
            if move_people == 2 and move_dragons == 0:
                print("Two people crossed back to the left side!")
            elif move_people == 0 and move_dragons == 2:
                print("Two dragons crossed back to the left side!")
            elif move_people == 1 and move_dragons == 1:
                print("One person and one dragon crossed back to the left side!")
        
        # Check if the game is won
        if left_people == 0 and left_dragons == 0:
            print_state(left_people, left_dragons, right_people, right_dragons, boat_position)
            print("🚀 Congratulations! You've successfully crossed the river!")
            break
    
    # Option to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        print("\nRestarting the game...\n")
        crossing_game()
    else:
        print("Thanks for playing! Goodbye!")

# Run the game
crossing_game()