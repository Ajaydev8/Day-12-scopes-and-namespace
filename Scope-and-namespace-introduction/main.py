#  SCOPE

# This comes in the category of global scope
enemies = 1


def increase_enemies():
    # a variable inside the function comes in the category of local_scope
    enemies = 2
    print(f"enemies inside the function: {enemies}")


increase_enemies()
print(f"enemies outside of the function: {enemies}")


# Local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# This will give error because it is outside the local scope and wrote individually.
print(potion_strength)



# Global scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)


# There is no Block scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Constant

# globla constants are always written in capital letters.
PI = 3.14159
URL = "https://www.google.com"