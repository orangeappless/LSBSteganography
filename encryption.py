from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()

    with open("keyfile.key", "wb") as keyfile:
        keyfile.write(key)


def encrypt(data):
    with open("keyfile.key", "rb") as keyfile:
        key = keyfile.read()

    fernet = Fernet(key)

    encrypted_data = fernet.encrypt(data)

    return encrypted_data


def decrypt(data):
    with open("keyfile.key", "rb") as keyfile:
        key = keyfile.read()

    fernet = Fernet(key)

    decrypted_data = fernet.decrypt(data.encode("utf-8"))
    original_data = decrypted_data.partition(b"$SOURCENAME")[0]
    original_file_name = decrypted_data.partition(b"$SOURCENAME")[2]

    output_string = (original_data.decode("utf-8") + "\n" + "Original file name: " + original_file_name.decode("utf-8"))

    with open("decrypted.txt", "wb") as file:
        file.write(output_string.encode("utf-8"))
