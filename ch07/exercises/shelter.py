import time
import uuid
class Shelter:
    def __init__(self, name, type):
        self.id = time.strftime("%Y%m%d%H%M%S")
        self.name = name
        self.type = type
        self.arrived = time.strftime("%d/%m/%Y")
        self.adopted = None
    def set_adopted(self):
        self.adopted = time.strftime("%d/%m/%Y")
    def __str__():
        result_str = f"{self.type}"
        result_str1 = f"{self.arrived}"
        # result_str
def main():
    fido = Shelter("fido", "cat")
    b = Shelter("Drake", "lizard")
main()