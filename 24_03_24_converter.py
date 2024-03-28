class Celsius(float):
    @classmethod
    def from_fahrenheit(cls, fahrenheit: "Fahrenheit") -> "Celsius":
        return Celsius((fahrenheit - 32) / 1.8)

    def to_fahrenheit(self) -> "Fahrenheit":
        return Fahrenheit.from_celsius(self)


class Fahrenheit(float):

    @classmethod
    def from_celsius(cls, celsius: Celsius) -> "Fahrenheit":
        return Fahrenheit(celsius * 1.8 + 32)

    def to_celsius(self) -> Celsius:
        return Celsius.from_fahrenheit(self)


class Meters(float):
    @classmethod
    def from_feet(cls, feet: "Feet") -> "Meters":
        return Meters(feet * 0.3048)

    def to_feet(self) -> "Feet":
        return Feet.from_meters(self)

class Feet(float):
    @classmethod
    def from_meters(cls, meters: "Meters") -> "Feet":
        return Feet(meters / 0.3048)

    def to_meters(self) -> Meters:
        return Meters.from_feet(self)

if __name__ == "__main__":
    line: str = input("Enter a temperature or a length: ")
    value: Fahrenheit | Celsius | Feet | Meters
    if line[-1] in "Ff":
        value = Fahrenheit(float(line[:-1]))
        print(f"{value}F = {value.to_celsius()}C")
    elif line[-1] in "Cc":
        value = Celsius(float(line[:-1]))
        print(f"{value}C = {value.to_fahrenheit()}F")
    elif line[-2:].lower() == "ft":
        value = Feet(float(line[:-2]))
        print(f"{value}ft = {value.to_meters()}m")
    elif line[-1].lower() == "m":
        value = Meters(float(line[:-1]))
        print(f"{value}m = {value.to_feet()}ft")
    else:
        print("Invalid input, value has to be in the format <number><F|C|ft|m>")
        quit(1)
