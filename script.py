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
    if length < 8:
        print("\nLength must be at least 8!\n")
        continue
    elif length >= 129:
        print("\nLength must not exceed 128 characters!\n")
        continue
    guaranteed = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS),
    ]
    chars = []
    for i in range(length - 4):
        chars.append(secrets.choice(alphabet))
    chars = guaranteed + chars
    rng = secrets.SystemRandom()
    rng.shuffle(chars)
    password = "".join(chars)
    print(f"\nYour password: {password} consisting of {length} characters\n")