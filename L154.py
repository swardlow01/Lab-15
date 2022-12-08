#sarah wardlow
class Fabric:
    def __init__(self, origin, color):
        self.origin = origin
        self.color = color

    def __str__(self):
        return self.origin + "("+ str(self.color) + ")"

f1 = Fabric("France", "blue")

print(f1)
