import enum


# fib = 1 : 1 : zipWith (+) fib (tail fib)
# {⊑(+`⌽)⍟𝕩 0‿1}

class Group(enum.IntEnum):
    Kid = 13
    Teenager = 20
    Adult = 65
    Senior = 0

    @classmethod
    def from_age(cls, age: int) -> "Group":
        if age < Group.Kid:
            return Group.Kid
        elif age < Group.Teenager:
            return Group.Teenager
        elif age < Group.Adult:
            return Group.Adult
        else:
            return Group.Senior


if __name__ == "__main__":
    age: int = int(input("How old are you? "))
    group: Group = Group.from_age(age)
    article: str = "an" if group.name[0].lower() in "aeiou" else "a"

    print(f"You are {article} {group.name.lower()}!")
