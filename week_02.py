def show_menu():
    print()
    print("=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")

def show_inventory(inventory):
    print()
    print("Your inventory:")

    if len(inventory) == 0:
        print("Your inventory is empty!")
    else:
        for item in inventory:
            print("-", item)

def can_buy(gold, price):
    if gold >= price:
        return True
    else:
        return False

def buy_item(gold, inventory, item_name, price):

    if can_buy(gold, price):
        gold = gold - price
        inventory.append(item_name)

        print()
        print("You bought a", item_name + "!")
        print("Remaining gold:", gold)

    else:
        print()
        print("You don't have enough gold!")

    return gold

print("Welcome to the Fantasy Item Shop!")

player_name = input("What is your name? ")

player_gold = 100
inventory = []

print()
print("Hello", player_name + "!")
print("You have", player_gold, "gold.")

shop_items = ["Sword", "Shield", "Potion", "Bow"]

print()
print("Items available in the shop:")

for item in shop_items:
    print("-", item)
    
shop_open = True

while shop_open:

    show_menu()

    choice = input("What would you like to do? ")

    match choice:

        case "1":
            player_gold = buy_item(
                player_gold, inventory, "Sword", 50
            )

        case "2":
            player_gold = buy_item(
                player_gold, inventory, "Shield", 40
            )

        case "3":
            player_gold = buy_item(
                player_gold, inventory, "Potion", 20
            )

        case "4":
            player_gold = buy_item(
                player_gold, inventory, "Bow", 60
            )

        case "5":
            show_inventory(inventory)

        case "6":
            print()
            print("Thanks for visiting,", player_name + "!")
            print("You have", player_gold, "gold left.")
            shop_open = False

        case _:
            print("Invalid choice! Please choose between 1 and 6.")

print("Shop closed.")
