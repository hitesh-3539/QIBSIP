import random
import string

def generate_password():
    print("\n=========================================")
    print("      RANDOM PASSWORD GENERATOR          ")
    print("=========================================\n")
    
    try:
        # Step 1: Get and validate password length
        length = int(input("Enter the desired password length (e.g., 12): "))
        if length < 4:
            print("\n❌ Error: Password length should be at least 4 characters for security.")
            return

        # Step 2: Get user preferences for character types
        print("\nSelect character sets to include:")
        include_letters = input("Include letters? (A-Z, a-z) [y/n]: ").strip().lower() == 'y'
        include_numbers = input("Include numbers? (0-9) [y/n]: ").strip().lower() == 'y'
        include_symbols = input("Include symbols? (!@#$...) [y/n]: ").strip().lower() == 'y'

        # Step 3: Build the character pool based on choices
        character_pool = ""
        mandatory_characters = []

        if include_letters:
            character_pool += string.ascii_letters
            # Ensure at least one letter is included
            mandatory_characters.append(random.choice(string.ascii_letters))
        if include_numbers:
            character_pool += string.digits
            # Ensure at least one digit is included
            mandatory_characters.append(random.choice(string.digits))
        if include_symbols:
            character_pool += string.punctuation
            # Ensure at least one symbol is included
            mandatory_characters.append(random.choice(string.punctuation))

        # Validation: Ensure at least one set was selected
        if not character_pool:
            print("\n❌ Error: You must select at least one character type!")
            return

        # Step 4: Fill the rest of the password length randomly from the pool
        remaining_length = length - len(mandatory_characters)
        random_characters = [random.choice(character_pool) for _ in range(remaining_length)]
        
        # Combine mandatory chars with random ones and shuffle to prevent predictable patterns
        password_list = mandatory_characters + random_characters
        random.shuffle(password_list)
        
        final_password = "".join(password_list)

        print("\n-----------------------------------------")
        print(f"🔑 Generated Password: {final_password}")
        print("-----------------------------------------")

    except ValueError:
        print("\n❌ Error: Invalid input. Please enter a valid whole number for length.")

if __name__ == "__main__":
    generate_password()