import random

# ------------------------------------------------------------
# SETUP
# ------------------------------------------------------------
print("--- Welcome to Mystery Island Escape! ---")
player_name = input("Enter your adventurer name: ")
score = 100
escaped = False
directions = ["north", "south", "east", "west"]
escape_dir = random.choice(directions)

print(f"Player name: {player_name}")
print(f"Starting Energy: {score}")
print(f"A secret escape direction has been chosen.")  # don't reveal escape_dir!

# ------------------------------------------------------------
# GAME LOOP (one fake round, no while yet)
# ------------------------------------------------------------
print("-" * 30)
print(f"ADVENTURER: {player_name} | ENERGY: {score}")
action = input("Where to? (jungle / beach / camp / quit): ").lower().strip()
print(f"Player chose: {action}")

# --- JUNGLE ---
print("The jungle is thick and spooky...")
jungle_guess = input("Which way leads to the ocean? (north/south/east/west): ").lower()
print(f"Player guessed: {jungle_guess}")
print("DEAD END! You spent hours hacking through vines.")
score -= 25
print(f"Energy after jungle: {score}")

print("-" * 30)
print(f"ADVENTURER: {player_name} | ENERGY: {score}")

# --- BEACH ---
print("You find a rusty treasure chest buried in the sand.")
beach_code = random.randint(1, 5)
beach_guess = input("Enter a 1-digit code (1-5) to unlock it: ")
print(f"Secret code was: {beach_code}")
print(f"Player guessed: {beach_guess}")
print("CLICK! You found energy bars and water! (+25 Energy)")
score += 25
print(f"Energy after beach: {score}")

print("-" * 30)
print(f"ADVENTURER: {player_name} | ENERGY: {score}")

# --- CAMP ---
print("You head back to your base camp to rest...")
luck = random.choice([True, False])
print(f"Luck: {luck}")
print("A group of monkeys raided your camp! (-20 Energy)")
score -= 20
print(f"Energy after camp: {score}")

print("-" * 30)
print(f"ADVENTURER: {player_name} | ENERGY: {score}")

# --- ESCAPE ---
print("The jungle is thick and spooky...")
escape_guess = input("Which way leads to the ocean? (north/south/east/west): ").lower()
print(f"Player guessed: {escape_guess}")
print("SUCCESS! You found a hidden boat and sailed away!")
escaped = True
print(f"escaped = {escaped}")

# ------------------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------------------
print()
print("=" * 30)
print(f"FINAL STATS FOR {player_name.upper()}")
print(f"Ending Energy: {score}")
print("RESULT: YOU ESCAPED THE ISLAND!")
print("=" * 30)
