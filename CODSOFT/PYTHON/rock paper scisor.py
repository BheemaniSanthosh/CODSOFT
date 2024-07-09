import random

def play_round(user_choice):
    

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

  
    if user_choice == computer_choice:
        winner = "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        winner = "User"
    else:
        winner = "Computer"

    return user_choice, computer_choice, winner

def main():
    # Track user and computer scores
    user_score = 0
    computer_score = 0

    while True:
       
        print("Welcome to Rock-Paper-Scissors!")
        print("Choose rock, paper, or scissors (or 'q' to quit): ")
        user_choice = input().lower()

        if user_choice == 'q':
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

      
        user_choice, computer_choice, winner = play_round(user_choice)

    
        print(f"You chose {user_choice}, computer chose {computer_choice}.")
        if winner == "Tie":
            print("It's a tie!")
        else:
            if winner == "User":
                print("You win!")
                user_score += 1
            else:
                print(f"You lose. {computer_choice} beats {user_choice}.")
                computer_score += 1

           
            print(f"Current score: User - {user_score}, Computer - {computer_score}")

     
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print(f"Thanks for playing! Final score: User - {user_score}, Computer - {computer_score}")

if __name__ == "__main__":
    main()
