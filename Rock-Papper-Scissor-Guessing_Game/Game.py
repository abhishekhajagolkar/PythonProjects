import random

print("""
🎮=======================================
      WELCOME TO ROCK ✊ PAPER 📄 SCISSORS ✂
=======================================
💡 Type 'rock', 'paper', or 'scissor' to play.
❌ Type 'exit' to quit anytime.
""")

Game = ("rock", "paper", "scissor")

while True:
    User_choice = input("\n🧑 Your move (rock 📄 / paper 📄 / scissor ✂): ").strip().lower()

    if User_choice == "exit":
        print("🚪 Thanks for playing! Goodbye! 👋")
        break

    if User_choice not in Game:
        print("⚠ Invalid move! Please choose rock, paper, or scissor.")
        continue

    Computer_choice = random.choice(Game)

    print(f"\n🧑 You chose: {User_choice}   🤖 Computer chose: {Computer_choice}")

    if User_choice == Computer_choice:
        print("🤝 It's a tie! Both chose the same.")
    
    elif User_choice == "rock":
        if Computer_choice == "paper":
            print("📄 Paper covers ✊ Rock — 💻 Computer Wins!")
        else:
            print("✊ Rock smashes ✂ Scissor — 🎉 You Win!")

    elif User_choice == "paper":
        if Computer_choice == "scissor":
            print("✂ Scissor cuts 📄 Paper — 💻 Computer Wins!")
        else:
            print("📄 Paper covers ✊ Rock — 🎉 You Win!")

    elif User_choice == "scissor":
        if Computer_choice == "rock":
            print("✊ Rock smashes ✂ Scissor — 💻 Computer Wins!")
        else:
            print("✂ Scissor cuts 📄 Paper — 🎉 You Win!")

