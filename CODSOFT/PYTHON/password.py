import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random.choices()
    password_list = random.choices(characters, k=length)
 
    password = ''.join(password_list)
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("\nEnter the length of the password you want to generate: "))
            
            if length <= 0:
                print("Length should be greater than zero. Please enter a valid length.")
                continue
            
            # Generate the password
            password = generate_password(length)
            
            # Print the generated password
            print(f"\nYour generated password of length {length} is:")
            print(password)
            
            break  
        
        except ValueError:
            print("Invalid input. Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
