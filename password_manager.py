import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    with open(filename, "r") as f:
        password = f.read().strip()
    encrypted_passwords = caesar_encrypt(password)

    with open(filename, "w") as f:
        f.write(encrypted_passwords)


def encrypt_passwords_in_file(filename: str) -> None:
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
    for index, row in enumerate(rows):
        if index!= 0:
            row[2] = caesar_encrypt(row[2])

    with open(filename, "w", newline="") as f:
         writer = csv.writer(f)
         writer.writerows(rows)

def change_password(filename: str, website: str, password: str) -> bool:
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
    for index, row in enumerate(rows):
        if row[0] == website:
            rows[index][2] = caesar_encrypt(password)
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            return True   
    return False
    


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    encrypted_password = caesar_encrypt(password)
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([website_name, username, encrypted_password])
    pass
