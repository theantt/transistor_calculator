import single_transistor_formulas.trans_bjt_formulas as bjt

# Standard values
v_t = 26e-3

"""CBA"""


# Set variables
variables = [
    47.4e3,     # rc
    0.3e3,      # re
    0.7e3,      # rb
    0,         # beta
    0,     # ic
    v_t         # vt
]

cba = bjt.CommonBaseAmplifier(variables)

# List of variables to print from class
print_list = [
    "max_av"
]

# Print in scientific format
for var in vars(cba):
    for x in print_list:
        if x == var:
            values = getattr(cba, var)
            print(var, " is  {:.2E}".format(values))
