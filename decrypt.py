from cryptography.fernet import Fernet
import sys
import os

CERTS_DIR = "/certs/"


def load_key(filename):
    """Load the encryption key from a file."""
    with open(filename, 'rb') as key_file:
        return key_file.read()


def decrypt_file(encrypted_file_path, key):
    """Decrypt the specified encrypted file using the provided key."""
    fernet = Fernet(key)

    with open(encrypted_file_path, 'rb') as enc_file:
        encrypted_data = enc_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    # Save decrypted data to a new file
    with open(encrypted_file_path.replace('.encrypted', '_decrypted.txt'), 'wb') as dec_file:
        dec_file.write(decrypted_data)


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "filename.txt.encrypted"

    # Load the previously saved encryption key
    key = load_key('secret.key')
    print(filename)
    # Specify the encrypted file to decrypt
    # Change this to your actual encrypted file path
    file_path = os.path.join(
        os.getcwd()+CERTS_DIR+filename)

    decrypt_file(file_path, key)

    print(f"\nFile '{file_path}' has been decrypted.\n")


if __name__ == "__main__":
    main()
