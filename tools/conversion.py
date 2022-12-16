import math

""" Basic conversions in decibels """


# USE CASE EXAMPLE: value_to_decibels(1000, "voltage") = 60
def value_to_decibels(my_input, my_type):
    if my_type == "voltage" or my_type == "current":
        output = 20 * math.log(my_input, 10)
        return output
    elif my_type == "power":
        output = 10 * math.log(my_input, 10)
        return output


# USE CASE EXAMPLE: value_from_decibels(60, "voltage") = 1000
def value_from_decibels(my_input, my_type):
    if my_type == "voltage" or my_type == "current":
        output = 10 ** (my_input / 20)
        return output
    elif my_type == "power":
        output = 10 ** (my_input / 10)
        return output


""" Low pass single pole/time constant response"""


def pole_frequency(r, c):
    w0 = 1 / (r * c)  # pole/corner frequency
    return w0


