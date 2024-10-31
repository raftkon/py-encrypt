from cryptography.fernet import Fernet
import os
import sys

CERTS_DIR = "/certs/"


def generate_key():
    """Generate a new Fernet key."""
    key = Fernet.generate_key()
    return key


def save_key(key, filename):
    """Save the encryption key to a file."""
    with open(filename, 'wb') as key_file:
        key_file.write(key)


def load_key(filename):
    """Load the encryption key from a file."""
    with open(filename, 'rb') as key_file:
        return key_file.read()


def encrypt_file(file_path, key):
    """Encrypt the specified file using the provided key."""
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


def main():
    try:
        if (len(sys.argv) < 2):
            raise Exception(
                "You must provide the filename of the file you want to encrypt.")
        filename = sys.argv[1]
        # Generate and save a custom key
        key = generate_key()
        save_key(key, 'secret.key')

        # # Specify the file to encrypt
        file_path = os.path.join(os.getcwd()+CERTS_DIR+filename)

        encrypt_file(file_path, key)

        print(
            f"\nFile '{file_path}' has been encrypted and saved as '{file_path}.encrypted'.\n")
        print("Encryption key saved as 'secret.key'.\n")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
