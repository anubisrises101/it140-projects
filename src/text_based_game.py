"""Project Two starter for the student's text-based adventure game."""

# Aisling Skye McKenzie


def show_instructions():
    """Display the game objective and available commands."""

    print("Welcome to threshing day!")
    print("You must collect all 6 items and face Codagh to win, or die trying.")
    print("Available commands: north, south, east, west")
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

    current_room = 'Great Hall'
    inventory = []
    valid_directions = ('north', 'south', 'east', 'west')

    show_instructions()
    
    while current_room != 'Forest':
        show_status(current_room, inventory, rooms)
        player_input = input("Please enter your move:")
        if player_input in rooms[current_room] and player_input in valid_directions:
            current_room = rooms[current_room][player_input]
        elif player_input not in rooms[current_room] and player_input in valid_directions:
            print("You can't go that way!")
        elif player_input.startswith("get "):
            requested_item = player_input.split(" ", 1)[1]
            if 'item' not in rooms[current_room]:
                print("There is no item to pick up here.")
            elif requested_item == rooms[current_room]['item']:
                inventory.append(rooms[current_room]['item'])
                print(f"You have picked up the {rooms[current_room]['item']}.")
                del rooms[current_room]['item']
            else:
                print("Invalid item. Please try again.")
        elif player_input == 'exit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid command. Please try again.")

    if current_room == 'Forest' and len(inventory) == 6:
        print("Congratulations! You have collected all items and bonded with Codagh! You win!")
    elif current_room == 'Forest' and len(inventory) < 6:
        print("You have reached Codagh without all the items. He has incenerated you!")
    else:
        print("You have exited the game.")

if __name__ == "__main__":
    main()
