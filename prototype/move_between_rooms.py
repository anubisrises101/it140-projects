# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}

# Set the player's starting room.
current_room = 'Great Hall'

# Continue gameplay until the player chooses to exit.
while current_room != 'exit':

    # Display the player's current room.
    print('You are in the', current_room)

    # Prompt the player for a movement command.
    movement_command = input('Enter your move: ').lower()

    # Exit the game if the player enters "exit".
    if movement_command == 'exit':
        current_room = 'exit'

    # Check whether the requested direction is valid from the current room.
    elif movement_command in rooms[current_room]:
        current_room = rooms[current_room][movement_command]

    # Handle invalid movement commands.
    else:
        print("Can't move that direction!")

print('Thanks for playing!')
