import math

import general_functions.mos.mos_fundamentals as mos_f

class MyTransistor:
    def __init__(self, config, val):
        # Set type
        self.type = config[0]
        self.mos_type = config[1]

        # Given constants
        self.i_d = val[0]
        self.i_s = val[1]
        self.i_g = val[2]

        self.rd = val[3]
        self.rs = val[4]
        self.rg = val[5]

        self.vt = val[6]
        self.wl = val[7]
        self.k = val[8]
        self.t_lambda = val[9]

        # Calculated or given inputs
        self.v_on = val[10]
        self.v_gs = val[11]
        self.v_sb = val[14]
        self.gamma = val[12]
        self.two_phi_f = val[13]
        self.va = val[14]

        if self.va is None and self.t_lambda is not None:
            self.va = 1 / self.t_lambda
        elif self.t_lambda is None and self.va is not None:
            self.t_lambda = 1 / self.va

        # Calculated
        self.r_o = None
        self.r_i = None

        self.Rid = None
        self.Ris = None
        self.Rie = None
        self.Gm = None


        # Calculate v_on if not given
        if self.v_on is None:
            self.v_on = mos_f.calc_v_on(self.v_gs, self.vt, self.k, self.i_d, self.wl)

        # Calculate ro
        # Triode or Saturation?
        if self.t_lambda is None:
            self.r_o = mos_f.calc_r_ds(self.k, self.wl, self.v_on)
        else:
            self.r_o = mos_f.r_ds(self.r_o, self.t_lambda, self.i_d)
            self.r_ds = self.r_o

        # Calculate transconductances
        self.gm = mos_f.calc_g_m(self.k, self.wl, self.v_on, self.i_d)
        self.g_mb = mos_f.calc_g_mb(self.gm, self.gamma, self.two_phi_f, self.v_sb)
        self.g_ds = 1 / self.r_o

        self.g_all = self.gm + self.g_mb + self.g_ds

        # low frequency input resistance
        self.r_i = 1 / self.gm



        # Calculate resistances "looking into"
        # Rid (R into drain) has infinite limit, larger than BJTs
        self.Rid = self.r_o * (1 + self.g_all * self.rs)
        # Ris (R into source)
        self.Ris = (1 / self.g_all) * (1 + (self.rd / self.r_o))
        # Rig (R into gate) is infinite at low frequencies
        self.Rig = math.inf

        # Calculate effective transconductance
        self.Gm = self.gm / (1 + self.g_all * self.rs)

        # Calculate currents and v_g
        if self.i_s is None:
            if self.i_d is not None:
                self.i_s = self.i_d
                self.v_g = self.i_d / self.Gm
        if self.i_d is None:
            if self.i_s is not None:
                self.i_d = self.i_s
                self.v_g = self.i_s / self.Gm

        if self.type == "CS":
            self.Ri = self.Rig

            # low frequency output resistance
            # self.r_o = ((self.rs ** -1) + (self.gm ** -1)) ** -1

            # self.Ro = ((self.rd ** -1) + (self.Rid ** -1)) ** -1
            print("NOTE: IF THIS IS A FEEDBACK LOOP, RO WILL BE: Ro = rd / (rg - rs)")
            #  Rd << Rid
            if self.rd < 10 * self.Rid:
                self.Ro = self.rd
                self.max_av = -(self.rd / self.rs)

            self.av = -(self.Gm * self.Ro)

        if self.type == "CG":
            self.Ri = self.Ris
            self.Ro = ((self.rd ** -1) + (self.Rid ** -1)) ** -1
            print("NOTE: IF THIS IS A FEEDBACK LOOP, Ro WILL BE: ???")
            #  Rd << Rid
            if self.rd < 10 * self.Rid:
                self.Ro = self.rd
                self.max_av = self.rd / self.rs

            self.av = (self.g_all * self.Ro) / (1 + (self.g_all * self.rs) + self.rd/self.r_o)

        if self.type == "CD":
            self.Ri = self.Rig
            self.Ro = ((self.rs ** -1) + (self.Ris ** -1)) ** -1
            print("NOTE: IF THIS IS A FEEDBACK LOOP, Ro WILL BE: ???")
            self.max_av = 1
            self.av = (self.gm * self.rs) / (1 + self.g_all * self.rs)
            if self.t_lambda and self.gamma is None:
                print(self.rs)
                self.av = (self.gm * self.rs) / (1 + self.g_m * self.rs)
            print("NOTE: IF THIS IS A FEEDBACK LOOP, av WILL BE: Rs/Rg")



# Set constants
vt = 26e-3
vtp = -0.5
vtn = 0.5
kp = 40e-6
kn = 100e-6

# May or may not be defined, set to None if not give
i_d = 149e-6
i_s = None
i_g = 0        # gate current is 0

wl = 61
k = kn
t_lambda = None
v_on = None
v_gs = None
v_sb = None
gamma = None
two_phi_f = None
va = None

# Resistors are always given
rd = 20.9e3
rs = 3.1e3
rg = 4.7e3

# Set defined configuration
amplifier = "CS"
bjt_type = "NMOS"

variables = [
    i_d,        # emitter current
    i_s,        # collector current
    i_g,        # base current
    rd,         # drain resistor
    rs,         # source resistor
    rg,         # gate resistor
    vt,         # thermal voltage
    wl,         # width-length ratio
    k,          # kn or kp
    t_lambda,   # lambda, MODELS CHANNEL LENGTH MODULATION
    v_on,       # "ON" voltage
    v_gs,       #
    gamma,      # MODELS BODY EFFECT
    two_phi_f,  #
    v_sb,       #
    va,         # early voltage
]

transistor_type = [
    amplifier,
    bjt_type,
]

amp = MyTransistor(transistor_type, variables)

# List of variables to print from class
print_list = [
    "r_i",      # low frequency input resistance
    "r_o",       # low frequency output resistance
    "gm",
    "g_mb",
    "max_av",
    "Ri",
    "Ro",
    "av"
]

# Print in scientific format
for val in vars(amp):
    for x in print_list:
        if x == val:
            values = getattr(amp, val)
            print(val, " is  {:.2E}".format(values))
