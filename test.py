from typing import List

print("imported test2")


class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f'Device {self.name!r} ({self.connected_by}): {"Connected" if self.connected else "Not connected"}'

    def __repr__(self):
        return f"Device(name={self.name!r}, connected_by={self.connected_by!r})"

    def disconnect(self):
        self.connected = False


printer = Device("Printer", "USB")
print(printer)
printer2 = eval(repr(printer))
printer2.disconnect()
print(printer2)


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


list_avg([123])


print("test.py: ", __name__)
