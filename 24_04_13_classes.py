class Resource:
    def __init__(self, state: str):
        self.state = state

class Manager:
    def __init__(self):
        self.resources = {}

    def add_resource(self, name: str, resource: Resource):
        self.resources[name] = resource

    def del_resource(self, name: str):
        del self.resources[name]

    def show(self):
        for k, v in self.resources.items():
            print(k, ":", v.state)

    def __getitem__(self, key: str):
        return self.resources[key]

if __name__ == "__main__":
    m = Manager()
    m.add_resource("r1", Resource("free"))
    m.add_resource("r2", Resource("busy"))
    m.add_resource("r3", Resource("free"))
    m.show()
    print("----")
    m.del_resource("r2")
    m.show()
    print("----")
    print("r1 is", m["r1"].state)