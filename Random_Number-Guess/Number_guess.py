import random 

# 🎯 Welcome to the Guess the Number Game!
print("\n🎮 WELCOME TO GUESS THE NUMBER GAME 🎯")
print("💡 Enter 0 anytime to exit\n")

ch = int(input("\n📌 Choose level:\n1️⃣ Easy (1-10)\n2️⃣ Medium (1-100)\n3️⃣ Hard (1-1000)\n➡ Your choice: "))

if ch == 1:
    random_number = random.randint(1, 10)
elif ch == 2:
    random_number = random.randint(1, 100)
elif ch == 3:
    random_number = random.randint(1, 1000)
else:
    print("⚠ Invalid Level! Shifting to Easy level (1-10):")
    random_number = random.randint(1, 10)

while True:
    guessed_number = int(input("🔢 Guess the number: "))
    if guessed_number == 0:
        print("🚪 EXIT — Thanks for playing! 👋")
        break
    elif guessed_number > random_number:
        print("📉 Your guess is too high! ⬇ Try again")
    elif guessed_number < random_number:
        print("📈 Your guess is too low! ⬆ Try again")
    else:
        print("🎉 Congratulations! You won the game 🏆")
        break

