class StringVar:
    def __init__(self, initial_value=""):
        self.__value = initial_value

    def set(self, new_value):
        self.__value = new_value

    def get(self):
        return self.__value

# Create an instance of StringVar
string_var = StringVar("Hello")

# Test the get method
print(string_var.get())  # Output: Hello

# Test the set method
string_var.set("Goodbye")
print(string_var.get())  # Output: Goodbye
