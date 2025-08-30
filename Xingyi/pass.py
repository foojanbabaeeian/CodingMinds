import os
import random
import string
import pyperclip
from cryptography.fernet import Fernet

# Function to generate a random password
def generate_password(length=12, complexity="medium"):
    """
    Generates a random password with specified length and complexity.
    
    Args:
        length (int): Length of the generated password (default is 12).
        complexity (str): Complexity level of the password (default is "medium").
        
    Returns:
        str: Generated password.
    """
    # Define character sets based on complexity
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Build the character pool based on complexity
    if complexity == "low":
        chars = lower_chars + digits
    elif complexity == "medium":
        chars = lower_chars + upper_chars + digits
    else:
        chars = lower_chars + upper_chars + digits + special_chars

    # Generate a random password using the character pool
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


# Function to encrypt a password using Fernet encryption
def encrypt_password(password):
    """
    Encrypts a password using Fernet encryption.
    
    Args:
        password (str): The password to be encrypted.
        
    Returns:
        str: Encrypted password (base64 encoded).
    """
    # Generate a key for encryption (This key should be securely stored)
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    
    # Encrypt the password
    encrypted_password = cipher_suite.encrypt(password.encode())
    
    # Store the key securely (in a real app, store this in a secure place)
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    
    return encrypted_password


# Function to store an encrypted password
def store_password(service_name, encrypted_password):
    """
    Stores an encrypted password along with the associated service name.
    
    Args:
        service_name (str): The name of the service (e.g., 'Google', 'Facebook').
        encrypted_password (str): The encrypted password to be stored.
    """
    # Save the encrypted password to a local file or database (here, using a simple text file)
    with open("passwords.txt", "a") as f:
        f.write(f"{service_name}: {encrypted_password.decode()}\n")


# Function to decrypt an encrypted password
def decrypt_password(encrypted_password):
    """
    Decrypts an encrypted password.
    
    Args:
        encrypted_password (str): The encrypted password to be decrypted.
        
    Returns:
        str: Decrypted password.
    """
    # Load the encryption key (ensure the key is securely stored and retrieved)
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    
    cipher_suite = Fernet(key)
    
    # Decrypt the password
    decrypted_password = cipher_suite.decrypt(encrypted_password.encode())
    
    return decrypted_password.decode()


# Function to search for a password associated with a service name
def search_password(service_name):
    """
    Searches for the encrypted password associated with a given service name.
    
    Args:
        service_name (str): The name of the service (e.g., 'Google', 'Facebook').
        
    Returns:
        str: The encrypted password for the service, if found, otherwise None.
    """
    # Search for the service in the password storage file
    with open("passwords.txt", "r") as f:
        for line in f:
            if line.startswith(service_name):
                # Extract the encrypted password from the line
                encrypted_password = line.split(":")[1].strip()
                return encrypted_password
    return None


# Function to copy the password to clipboard
def copy_to_clipboard(password):
    """
    Copies the password to the clipboard.
    
    Args:
        password (str): The password to copy to the clipboard.
    """
    # Use the pyperclip library to copy the password to the clipboard
    pyperclip.copy(password)


# Function to load stored passwords (read from file)
def load_passwords():
    """
    Loads stored encrypted passwords from the local file.
    
    Returns:
        list: A list of stored service names and encrypted passwords.
    """
    passwords = []
    with open("passwords.txt", "r") as f:
        for line in f:
            service_name, encrypted_password = line.split(":")
            passwords.append((service_name.strip(), encrypted_password.strip()))
    return passwords


# Function to save passwords to the storage file
def save_passwords(service_name, encrypted_password):
    """
    Saves the encrypted password to the local file.
    
    Args:
        service_name (str): The name of the service (e.g., 'Google', 'Facebook').
        encrypted_password (str): The encrypted password to be saved.
    """
    store_password(service_name, encrypted_password)

