import time


class System:
    def __init__(self):
        self.reservations = {}

    def add_reservation(self, name, duration: float):
        if name not in self.reservations:
            raise KeyError("Object does not exist")

        if self.reservations[name] is not None:
            raise ValueError("Object is already reserved")

        self.reservations[name] = time.time() + duration

    def remove_reservation(self, name):
        if name not in self.reservations:
            raise KeyError("Object does not exist")

        if self.reservations[name] is None:
            raise ValueError("Object is not reserved")

        if time.time() > self.reservations[name]:
            print("Shame on you for being late")
        self.reservations[name] = None

    def register(self, name):
        if name in self.reservations:
            raise KeyError("Object already exists")
        self.reservations[name] = None

    def unregister(self, name):
        if name not in self.reservations:
            raise KeyError("Object does not exist")
        del self.reservations[name]

    def show(self):
        for k, v in self.reservations.items():
            print(k, ":",
                  "Available" if v is None else
                  time.strftime("Rented until %Y-%m-%d %H:%M:%S", time.gmtime(v))
                  )


if __name__ == "__main__":
    s = System()
    s.register("r1")
    s.register("r2")
    s.register("r3")
    s.add_reservation("r2", 5)
    s.add_reservation("r3", 10)
    s.show()
    time.sleep(8)
    s.show()
    s.remove_reservation("r2")
    s.remove_reservation("r3")
    s.show()

