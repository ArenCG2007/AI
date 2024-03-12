# Programmer: Aren Gay
# Date 3.12.2024
# Program: Password Generator
# Source: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib


def hash_password(password, salt):
    # Combine password and salt
    salted_password = password + salt

    # Hash the salted password using SHA-256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

    return hashed_password


def main():
    # Accept password input from the user
    password = input("Enter your password: ")

    # Choose a salt (you can generate a random one for better security)
    salt = "mysalt123"

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed password:", hashed_password)


if __name__ == "__main__":
    main()
