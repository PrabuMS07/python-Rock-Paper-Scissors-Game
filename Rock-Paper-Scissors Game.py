import random

def main():
    scores = [0, 0]
    while True:
        user = input("Choose rock, paper, or scissors: ").lower()
        if user not in ['rock', 'paper', 'scissors']: continue
        computer = random.choice(['rock', 'paper', 'scissors'])
        print(f"You: {user}, Computer: {computer}")
        
        if user == computer: print("Tie!")
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'scissors' and computer == 'paper') or \
             (user == 'paper' and computer == 'rock'): 
            scores[0] += 1; print("You win!")
        else: 
            scores[1] += 1; print("You lose!")
        
        print(f"Score: You {scores[0]} - Computer {scores[1]}")
        if input("Play again? (y/n): ").lower() != 'y': break

    print("Bye!")

if __name__ == "__main__":
    main()
