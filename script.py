 import secrets

chars = []

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+"

alphabet = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS

while True:
    raw = input("\nEnter the number of characters the password should consist of (Exit — 'x'): ")
    if raw.lower() == "x":
        print("Thank you for using!")
        break
    length = int(raw)
    chars = []
    for i in range(length):
        chars.append(secrets.choice(alphabet))
    password = "".join(chars)
    print(f"\nYour password: {password} consisting of {length} characters\n")