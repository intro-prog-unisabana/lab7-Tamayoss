import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    with open(filename, "r") as f:
        password = f.read().strip()
    encrypted_passwords = caesar_encrypt(password)

    with open(filename, "w") as f:
        f.write(encrypted_passwords)

    if __name__ == "__name__":
        encrypt_single_pass("password.txt")
    pass  


def encrypt_passwords_in_file(filename: str) -> None:
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = [row for row in reader] 
    
    for row in rows:
        row[2] = caesar_encrypt(row[2])
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    pass

def change_password(filename: str, website: str, password: str) -> bool:
    with open(filename, "w", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
