from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    filename = input("Enter the CSV file name:\n").strip()
    encrypt_passwords_in_file(filename)

    while True:
        option = input("Options: (1) Change Password, (2) Add Password, (3) Quit:\n").strip()
        if option == "1":
            user_input = input("Enter the website and the new password:\n").split()
            if len(user_input) < 2:
                print("Input is in the wrong format!")
                continue
            website, new_password = user_input[0], user_input[1]
            if len(new_password) < 12:
                print("Password is too short!")
                continue
            success = change_password(filename, website, new_password)
            print("Password changed." if success else "Website not found! Operation failed.")

        elif option == "2":
            user_input = input("Enter the website, username, and password:\n").split()
            if len(user_input) < 3:
                print("Input is in the wrong format!")
                continue
            website, username, password = user_input[0], user_input[1], user_input[2]
            if len(password) < 12:
                print("Password is too short!")
                continue
            add_login(filename, website, username, password)
            print("Login added.")

        elif option == "3":
            print("Exiting program...")
            break   
        else:
            print("Invalid option selected!")
    pass


if __name__ == "__main__":
    main()
