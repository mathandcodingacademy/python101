# Filename: mystery_island_escape.py
# A Text Adventure Game for Python Beginners

import random

# ------------------------------------------------------------
# 1. SETUP
# ------------------------------------------------------------
print("--- Welcome to Mystery Island Escape! ---")
player_name = input("Enter your adventurer name: ")

score = 100  # This represents your 'Survival Energy'
escaped = False

# Pick the hidden escape direction ONCE at the start
directions = ["north", "south", "east", "west"]
escape_dir = random.choice(directions)

# ------------------------------------------------------------
# 2. MAIN GAME LOOP
# ------------------------------------------------------------
while True:
    print("-" * 30)
    print(f"ADVENTURER: {player_name} | ENERGY: {score}")
    
    # 3. ASK FOR ACTION
    action = input("Where to? (jungle / beach / camp / quit): ").lower().strip()

    # 4. VALIDATE ACTION
    if action not in ["jungle", "beach", "camp", "quit"]:
        print("Invalid choice! You wander in circles and waste time.")
        continue  # Skips back to the start of the loop

    # 5. ACTION: QUIT
    if action == "quit":
        print(f"{player_name} decided to build a hut and live here forever.")
        break

    # 6. ACTION: JUNGLE (The Escape Mechanic)
    elif action == "jungle":
        print("\nThe jungle is thick and spooky...")
        guess = input("Which way leads to the ocean? (north/south/east/west): ").lower()
        
        if guess not in directions:
            print("That's not a direction! You got lost.")
            score -= 10
        elif guess == escape_dir:
            print("SUCCESS! You found a hidden boat and sailed away!")
            escaped = True
            break # Exit loop because we won!
        else:
            print("DEAD END! You spent hours hacking through vines.")
            score -= 25

    # 7. ACTION: BEACH (Mini-game using int conversion)
    elif action == "beach":
        print("\nYou find a rusty treasure chest buried in the sand.")
        code = random.randint(1, 5)
        guess_str = input("Enter a 1-digit code (1-5) to unlock it: ")

        # Check if input is a number before converting
        if guess_str.isdigit():
            guess = int(guess_str)
            
            if guess < 1 or guess > 5:
                print("The lock doesn't even have that number.")
                continue

            if guess == code:
                print("CLICK! You found energy bars and water! (+25 Energy)")
                score += 25
            else:
                print(f"WRONG! The code was {code}. You wasted your strength.")
                score -= 15
        else:
            print("That's not a number! You kicked the chest in frustration.")
            score -= 5

    # 8. ACTION: CAMP (Boolean Logic & Random Events)
    elif action == "camp":
        print("\nYou head back to your base camp to rest...")
        
        # LOGIC: If you are weak (score < 50) AND lucky, you get a big boost
        luck = random.choice([True, False])
        
        if score < 50 and luck:
            print("A local guide found you and shared a feast! (+50 Energy)")
            score += 50
        elif score >= 50:
            print("It's a nice day, but you're not getting any closer to home.")
            score -= 5
        else:
            print("A group of monkeys raided your camp! (-20 Energy)")
            score -= 20

    # 9. SCORE CHECK (Lose Condition)
    if score <= 0:
        score = 0
        print("\n--- GAME OVER ---")
        print("Your energy hit 0. You collapsed in the sand.")
        break

# ------------------------------------------------------------
# 10. FINAL SUMMARY
# ------------------------------------------------------------
print("\n" + "=" * 30)
print(f"FINAL STATS FOR {player_name.upper()}")
print(f"Ending Energy: {score}")

if escaped:
    print("RESULT: YOU ESCAPED THE ISLAND!")
else:
    print("RESULT: LOST ON THE ISLAND")
print("=" * 30)
