import random

opts = ["rock", "paper", "scissors"]
uscore = 0
cscore = 0

while True:
    u = input("Choose rock/paper/scissors: ").lower()
    if u not in opts:
        print("Invalid choice")
        continue

    c = random.choice(opts)
    print(f"Computer chose: {c}")

    if u == c:
        print("It's a tie!")
    elif (u == "rock" and c == "scissors") or (u == "paper" and c == "rock") or (u == "scissors" and c == "paper"):
        print("You win!")
        uscore += 1
    else:
        print("Computer wins!")
        cscore += 1

    print(f"Score - You: {uscore}  Computer: {cscore}")

    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        break

print("Thanks for playing!")