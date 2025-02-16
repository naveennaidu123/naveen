import random
import string

def generate_password(length=12):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the pool and generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example usage:
password_length = int(input("Enter the desired length of the password: "))
print(f"Generated password: {generate_password(password_length)}")
