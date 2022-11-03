import time
import uuid
class Shelter:
    def __init__(self, name, type):
        self.id = time.strftime("%Y%m%d%H%M%S")
        self.name = name
        self.type = type
        self.arrived = time.strftime("%Y/%m/%d")
        self.adopted = None
    def set_adopted(self):
        self.adopted = time.strftime("%Y/%m/%d")
    def __str__(self):
        result_str = f"{self.name}[{self.type}]"
        result_str += f"\narrived: {self.arrived}"
        result_str += f"\nadopted:{self.adopted}"
        return result_str
        # result_str
def main():
      fido = Shelter("Drake", "lizard")
      fido.set_adopted()
      print(fido)
main()