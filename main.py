    # main.py
from modialize import greet, MyClass

    # Using the function from my_module
message = greet("World")
print(message)

    # Using the class from my_module
my_object = MyClass(10)
print(f"Doubled value: {my_object.get_value()}")