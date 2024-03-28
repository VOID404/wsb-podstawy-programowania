import getpass

if __name__ == "__main__":
    password: str = getpass.getpass("Password: ")
    rules = {
        "Password is too short": lambda p: len(p) >= 8,
        "Password has to contain at least one digit": lambda p: any(c.isdigit() for c in p),
        "Password has to contain at least one uppercase letter": lambda p: any(c.isupper() for c in p),
        "Password has to contain at least one lowercase letter": lambda p: any(c.islower() for c in p),
    }

    for rule, condition in rules.items():
        if not condition(password):
            print(rule)
            quit(1)

    print("Password is valid")