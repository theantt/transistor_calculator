import single_transistor_formulas.trans_mos_formulas as mos

#Set variables
variables = [
    42.5e3,     # rd
    0.6e3,      # rs
    5.7e3,      # rg
    87,         # wl
    618e-6,     # id
    0.5,        # vt
    40e-6,     # k
    0,       # t_lambda
    0,          # gamma
    0,          # two_phi_f
    0           # vsb
]

amp = mos.CommonSourceAmplifier(variables)
# amp = mos.CommonGateAmplifier(variables)
# amp = mos.CommonDrainAmplifier(variables)

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
for var in vars(amp):
    for x in print_list:
        if x == var:
            values = getattr(amp, var)
            print(var, " is  {:.2E}".format(values))
