"""Project Two starter for the student's text-based adventure game."""

# Aisling Skye McKenzie


def show_instructions():
    """Display the game objective and available commands."""

    print("Welcome to threshing day!")
    print("You must collect all 6 items and face Codagh to win, or die trying.")
    print("Available commands: go north, go south, go east, go west")
    print("To add an item to inventory type 'get <item name>'")
    print("To exit the game type 'exit'")

def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""

    print(f"You are currently in the {current_room}.")
    print(f"You have the following items in your inventory: {', '.join(inventory) if inventory else 'none'}.")
    print(f"Currently this room has the following items: {rooms[current_room].get('item', 'none')}.")

def main():
    """Run the main gameplay loop."""

    rooms = {
        'Great Hall': {'south': 'Armory', 'north': 'Archives', 'east': 'Dining Hall', 'west': 'Training yard'},
        'Armory': {'north': 'Great Hall', 'item': 'Shortsword'},
        'Archives': {'south': 'Great Hall', 'east': 'Threshing grounds', 'west': 'Healers quad', 'item': 'Dragon guide'},
        'Dining Hall': {'west': 'Great Hall', 'north': 'Threshing grounds', 'item': 'Rations'},
        'Training yard': {'east': 'Great Hall', 'north': 'Healers quad', 'item': 'Harness'},
        'Threshing grounds': {'south': 'Dining Hall', 'west': 'Archives', 'north': 'Forest', 'item': 'Protective gear'},
        'Healers quad': {'east': 'Archives', 'south': 'Training yard', 'item': 'Healing kit'},
        'Forest': {'south': 'Threshing grounds', 'item': 'Codagh'} #final boss
    }

    # TODO: Set the player's starting room.

    # TODO: Create the player's inventory.

    # TODO: Call the instruction function at the appropriate time.

    # TODO: Create the gameplay loop.
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    pass


if __name__ == "__main__":
    main()
