user_score = 0
computer_score = 0
rounds = 0

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    
    if user_choice == "quit":
        print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("❌ Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"🖥️ Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("⚖️ It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("🎉 You win this round!")
        user_score += 1
    else:
        print("😢 You lose this round!")
        computer_score += 1
    
    rounds += 1
    print(f"📊 Score -> You: {user_score} | Computer: {computer_score}")
    print("-" * 30)
# Rock-Paper-Scissor
