import single_transistor_formulas.trans_bjt_formulas

# Standard values
v_t = 26e-3

"""CEA"""
# Set variables
variables = [
    23.8e3,     # rc
    0.1e3,      # re
    0.3e3,       # rb
    81,        # beta
    264e-6,     # ic
    0,         # va
    v_t         # vt
]

cea = single_transistor_formulas.trans_bjt_formulas.CommonEmitterAmplifier(variables)

# List of variables to print from class
print_list = [
    "max_av",
    "ri",
    "gm",
    "rpi",
    "Ro",
    "av"
]

# Print in scientific format
for var in vars(cea):
    for x in print_list:
        if x == var:
            values = getattr(cea, var)
            print(var, " is  {:.2E}".format(values))
