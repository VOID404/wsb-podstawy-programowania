if __name__ == "__main__":
    val: int = int(input("Number: "))
    print(f"{val} is {['even', 'odd'][val % 2]}")
