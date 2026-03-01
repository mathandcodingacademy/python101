# ------------------------------------------------------------
# SETUP
# ------------------------------------------------------------
print("--- Welcome to Mystery Island Escape! ---")
print("Player name: Alex")
print("Starting Energy: 100")
print("A secret escape direction has been chosen.")

# ------------------------------------------------------------
# GAME LOOP (one fake round)
# ------------------------------------------------------------
print("-" * 30)
print("ADVENTURER: Alex | ENERGY: 100")
print("Player chose: jungle")

# --- JUNGLE ---
print("The jungle is thick and spooky...")
print("Player guessed: north")
print("DEAD END! You spent hours hacking through vines.")
print("Energy after jungle: 75")

print("-" * 30)
print("ADVENTURER: Alex | ENERGY: 75")
print("Player chose: beach")

# --- BEACH ---
print("You find a rusty treasure chest buried in the sand.")
print("Secret code was: 3")
print("Player guessed: 3")
print("CLICK! You found energy bars and water! (+25 Energy)")
print("Energy after beach: 100")

print("-" * 30)
print("ADVENTURER: Alex | ENERGY: 100")
print("Player chose: camp")

# --- CAMP ---
print("You head back to your base camp to rest...")
print("Luck: False")
print("A group of monkeys raided your camp! (-20 Energy)")
print("Energy after camp: 80")

print("-" * 30)
print("ADVENTURER: Alex | ENERGY: 80")
print("Player chose: jungle")

# --- ESCAPE ---
print("The jungle is thick and spooky...")
print("Player guessed: east")
print("SUCCESS! You found a hidden boat and sailed away!")
print("escaped = True")

# ------------------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------------------
print()
print("=" * 30)
print("FINAL STATS FOR ALEX")
print("Ending Energy: 80")
print("RESULT: YOU ESCAPED THE ISLAND!")
print("=" * 30)
