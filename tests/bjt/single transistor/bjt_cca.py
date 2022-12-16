import single_transistor_formulas.trans_bjt_formulas as bjt

# Standard values
v_t = 26e-3

"""CCA"""
# Set variables
variables = [
    46.7e3,     # rc
    1.6e3,      # re
    0.3e3,      # rb
    49,         # beta
    639e-6,     # ic
    v_t         # vt
]

cca = bjt.CommonCollectorAmplifier(variables)

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
for var in vars(cca):
    for x in print_list:
        if x == var:
            values = getattr(cca, var)
            print(var, " is  {:.2E}".format(values))