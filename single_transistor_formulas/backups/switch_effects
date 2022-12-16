variables = [1]

class MyClass:
    def __init__(self, var):
        self.CLM = "Channel-length modulation automatically neglected"  #CWM
        self.BE = "Body effect neglected"
        self.vt = variables[0]

    def switchCLM(self, value):
        switch1 = {
            True: {
                "CLM": "Channel Length Modulation in effect",
                "vt": self.vt,
            },
            False: {
                "CLM": "Channel Length Modulation Neglected",
                "vt": 0,
            }
        }
        self.__dict__.update(switch1.get(value, {}))

    def switchBE(self, value):
        switch2 = {
            True: {
                "BE": "Body effect in effect",
            },
            False: {
                "CLM": "Body effect neglected",
            }
        }
        self.__dict__.update(switch2.get(value, {}))


# Create an instance of MyClass with default values
my_class = MyClass(variables)

# Print the values of var1 and var2
print(my_class.CLM)  # None
print(my_class.vt)  # None
print(my_class.BE)  # None

# Switch the values of var1 and var2 to True
my_class.switchCLM(True)

# Print the values of var1 and var2
print(my_class.CLM)  # True
print(my_class.vt)
print(my_class.BE)  # False

# Switch the values of var1 and var2 to False
my_class.switchBE(True)

# Print the values of var1 and var2
print(my_class.CLM)  # True
print(my_class.vt)  #
print(my_class.BE)  # True
