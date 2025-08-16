balance = 0

def check_balance():
    print("💰 Your balance is: ₹", balance)

def deposit_cash(amt):
    global balance
    balance += amt
    print(f"✅ {amt} ₹ deposited.")

def withdraw_cash(amt):
    global balance
    if amt > balance:
        print(f"⚠️ Insufficient balance! You have ₹ {balance}")
    else:
        balance -= amt
        print(f"💸 {amt} ₹ withdrawn.")

print("🏦 Welcome to Bank 🏦")

while True:
    choice = int(input("👉 Enter choice: \n1️⃣  Check Balance\n 2️⃣  Deposit Cash\n 3️⃣  Withdraw Cash\n 4️⃣  Exit "))

    if choice == 1:
        check_balance()
        
    elif choice == 2:
        amount = int(input("💵 Enter amount to deposit: ₹"))
        deposit_cash(amount)
        
    elif choice == 3:
        amount = int(input("💵 Enter amount to withdraw: ₹"))
        withdraw_cash(amount)
        
    elif choice == 4:
        print("👋 Thank you! Goodbye.")
        break
    else:
        print("❌ Invalid choice. Please enter 1-4.")
