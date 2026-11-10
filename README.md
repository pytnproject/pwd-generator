```markdown
# Password Generator

![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

Generates a random password of a specified length (8 to 128 characters) with a guaranteed inclusion of lowercase and uppercase letters, digits, and special characters, using the cryptographically secure `secrets` module and shuffling via `SystemRandom`.

# Features

- Interactive input of password length (from 8 to 128 characters).
- Guaranteed presence of at least one character from each category: lowercase letters, uppercase letters, digits, special characters.
- Remaining characters are selected from the full alphabet.
- Shuffling of the final password via `secrets.SystemRandom` for cryptographic security.
- Handling of invalid input (non-numeric values).
- Exit the program with the `x` command.

# Requirements

- Python 3.6+
- Standard library (`secrets`)

# Usage

```bash
python main.py
```


<details>
<summary>Example output</summary>

```
Enter the number of characters the password should consist of (Exit — 'x'): 12

Your password: aB3$kL9mN2pQ consisting of 12 characters

Enter the number of characters the password should consist of (Exit — 'x'): 5

Length must be at least 8!

Enter the number of characters the password should consist of (Exit — 'x'): abc

Enter a number!

Enter the number of characters the password should consist of (Exit — 'x'): x
Thank you for using!
```

</details>

<details>
<summary>Show code</summary>

```python
import secrets

chars = []

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+"

alphabet = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS

while True:
    try:
        raw = input("\nEnter the number of characters the password should consist of (Exit — 'x'): ")
        if raw.lower() == "x":
            print("Thank you for using!")
            break
        length = int(raw)    
        if length < 8:
            print("\nLength must be at least 8!\n")
            continue
        elif length >=129:
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
    except ValueError:
        print("\nEnter the number!\n")
```

</details>
```