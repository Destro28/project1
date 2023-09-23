import random

# Define a list of positive affirmations.
affirmations = [
    "I am capable of achieving my goals.",
    "I am deserving of love and happiness.",
    "I am resilient and can overcome challenges.",
    "I am grateful for the abundance in my life.",
    "I believe in my abilities and inner strength.",
]

# Initialize an empty list to store collected cards.
collected_cards = []

def display_menu():
    print("Positive Affirmation Card Collection Game")
    print("1. Draw a card")
    print("2. View collected cards")
    print("3. Quit")

def draw_card():
    affirmation = random.choice(affirmations)
    print("\nYou drew a card:")
    print(affirmation)
    collected_cards.append(affirmation)

def view_collected_cards():
    print("\nCollected Cards:")
    for i, card in enumerate(collected_cards, 1):
        print(f"{i}. {card}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            draw_card()
        elif choice == "2":
            view_collected_cards()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
