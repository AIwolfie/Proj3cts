from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Secret key generated and saved as 'secret.key'.")

def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Error: Secret key file not found. Please generate a key first.")
        return None

def encrypt_file(input_file, output_file, key):
    try:
        if not os.path.isfile(input_file):
            print(f"Error: The input file '{input_file}' does not exist.")
            return
        if os.path.isdir(output_file):
            print("Error: The output path is a directory. Please provide a valid file name for the output.")
            return
        with open(input_file, "rb") as file:
            data = file.read()
        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(data)
        with open(output_file, "wb") as file:
            file.write(encrypted_data)
        print(f"File '{input_file}' encrypted successfully and saved as '{output_file}'.")
    except Exception as e:
        print(f"Error encrypting file: {e}")

def decrypt_file(input_file, output_file, key):
    try:
        if not os.path.isfile(input_file):
            print(f"Error: The input file '{input_file}' does not exist.")
            return
        if os.path.isdir(output_file):
            print("Error: The output path is a directory. Please provide a valid file name for the output.")
            return
        with open(input_file, "rb") as file:
            encrypted_data = file.read()
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(output_file, "wb") as file:
            file.write(decrypted_data)
        print(f"File '{input_file}' decrypted successfully and saved as '{output_file}'.")
    except Exception as e:
        print(f"Error decrypting file: {e}")

def main():
    while True:
        print("\nFile Encryption/Decryption Tool")
        print("---------------------------------")
        print("1. Generate Secret Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            generate_key()
        elif choice == "2":
            key = load_key()
            if key:
                input_file = input("Enter the path of the file to encrypt: ").strip()
                output_file = input("Enter the path to save the encrypted file: ").strip()
                encrypt_file(input_file, output_file, key)
        elif choice == "3":
            key = load_key()
            if key:
                input_file = input("Enter the path of the file to decrypt: ").strip()
                output_file = input("Enter the path to save the decrypted file: ").strip()
                decrypt_file(input_file, output_file, key)
        elif choice == "4":
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
