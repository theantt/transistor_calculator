import general_functions.bjt.bjt_fundamentals as bjt_f

class MyTransistor:
    def __init__(self, config, var):
        # Set type
        self.type = config[0]
        self.bjt_type = config[1]

        # Given constants
        self.ie = var[0]
        self.ic = var[1]
        self.ib = var[2]

        self.re = var[6]
        self.rc = var[7]
        self.rb = var[8]

        # Calculated or given inputs
        self.alpha = var[3]
        self.beta = var[4]
        self.vt = var[5]

        self.va = var[9]

        # Calculated
        self.av = None
        self.rpi = None
        self.ro = None
        self.Ri = None

        self.Rie = None
        self.Ric = None
        self.Rib = None

        # Find currents
        if self.ib is None:
            if self.beta and self.ic is not None:
                self.ib = self.ic / self.beta

        # Calculate transconductance
        self.gm = bjt_f.gm(self.ic, self.vt)

        # Calculate ro
        if self.va is not None:
            self.ro = bjt_f.r_o(self.bjt_type, self.va, self.ic, self.vt)
        elif self.va is None:
            # Assume high resistance
            self.ro = 10e20

        # Calculate rpi
        self.rpi = bjt_f.r_pi(self.ic, self.beta, self.vt)

        """Calculate resistances "looking into"""
        # R into base
        self.Rib = self.rpi + ((self.beta + 1) * self.re)
        # R into emitter
        self.Rie = ((self.rpi + self.rb) / (self.beta + 1)) * (1 + (self.rc / self.ro))
        # R into collector
        if self.gm * self.re < self.beta:
            self.Ric = self.ro * (1 + self.gm * self.re)
        if self.gm * self.re > self.beta:
            self.Ric = self.ro * (1 + self.beta)

        # Common Emitter Amplifier
        if self.type == "CE":
            self.Ri = self.Rib
            # Rc << Ric
            if self.rc < 10 * self.Ric:
                self.Ro = self.rc
                self.vo = -(self.beta * self.ib * self.rc)
                self.max_av = -(self.rc / self.re)
            else:
                self.Ro = ((self.rc ** -1) + (self.Ric ** -1)) ** -1
                self.vo = -(self.beta * self.ib * self.Ro)
            self.av = -(self.beta * self.Ro) / (self.rb + self.Ri)

        # Common Base Amplifier
        if self.type == "CB":
            self.Ri = self.Rie

            # Rc << ro
            if self.rc < 10 * self.ro:
                self.Ri = (self.rpi + self.rb) / (self.beta + 1)
            # Rc << Ric
            if self.rc < 10 * self.Ric:
                self.max_av = (self.rc / self.re)
                self.Ro = self.rc
            else:
                self.Ro = ((self.rc ** -1) + (self.Ric ** -1)) ** -1
            self.av = (self.beta * self.Ro) / (self.rb + self.Rib)

        # Common Collector Amplifier
        if self.type == "CC":
            self.Ri = self.Rie
            # Rc << ro
            if self.rc < 10 * self.ro:
                self.Ro = ((self.re ** -1) + (((self.rpi + self.rb) / (self.beta + 1)) ** -1)) ** -1
            else:
                self.Ro = ((self.re ** -1) + (self.Ric ** -1)) ** -1
            self.av = ((self.beta + 1) * self.re) / (self.rb + self.Ri)
            self.max_av = 1

# Set constants
vt = 26e-3

# Set defined variables, set to None if not given
ie = None
ic = 283e-6
ib = None
alpha = None
beta = 34
va = 10

rc = 36.9e3
re = 0.8e3
rb = 0.2e3

# Set defined configuration
amplifier = "CB"
bjt_type = "PNP"

variables = [
    ie,     # emitter current
    ic,     # collector current
    ib,     # base current
    alpha,  # current gain ic/ie
    beta,   # forward current gain (ic/ib)
    vt,     # thermal voltage
    re,     # emitter resistance
    rc,     # collector resistance
    rb,     # base resistance
    va,     # early voltage
]

transistor_type = [
    amplifier,
    bjt_type,
]

amp = MyTransistor(transistor_type, variables)

# List of variables to print from class
print_list = [
    "max_av",
    "r_o",
    "Ro",
    "av",
    "gm"
]

# Print in scientific format
for var in vars(amp):
    for x in print_list:
        if x == var:
            values = getattr(amp, var)
            print(var, " is  {:.2E}".format(values))
