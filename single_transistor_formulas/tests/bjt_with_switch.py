import math


class BjtAmplifier:
    def __init__(self, vals):
        # Set given constants
        self.rc = vals[0]
        self.re = vals[1]
        self.rb = vals[2]
        self.beta = vals[3]
        self.ic = vals[4]
        self.va = vals[5]
        self.vt = vals[6]

        # Other constants that may be provided
        self.cje0 = None
        self.tau_f = None
        self.cu0 = None
        self.vbc = None
        self.phi0c = None
        self.phi0s = None
        self.cs0 = None
        self.vsc = None

        """ Initialize transistor options"""
        # Set effects
        # Ignore effects of CLM and BE
        self.CLM = None
        self.BE = None

        # Set transistor
        self.transistor = None
        self.bjt = None

        # Set variables to be defined in functions later

        """ Basic BJT """
        # Small-signal forward active
        self.gm = None
        self.rpi = None
        self.ri = None
        self.ro = None
        self.uf = None
        self.cb = None
        self.cpi = None
        self.cje = None
        self.cu = None
        self.cs = None
        self.ft = None

        """ Single BJT Transistor """
        self.av = None
        self.max_av = None
        self.Ro = None

    def switchCLM(self, value):
        if value == 1:
            self.CLM = 1
        elif value == 0:
            self.CLM = 0
        else:
            print("Please enter 1 or 0 to set the value of CLM")

    def switchBE(self, value):
        if value == 1:
            self.BE = 1
        elif value == 0:
            self.BE = 0
        else:
            print("Please enter 1 or 0 to set the value of BE")

    def transistorType(self, value):
        if value == "CBA":
            self.transistor = "CBA"
        elif value == "CCA":
            self.transistor = "CCA"
        elif value == "CEA":
            self.transistor = "CEA"
        else:
            print("Please set the transistor type to one of the following: CBA, CCA, or CEA")

    def bjtType(self, value):
        if value == "NPN":
            self.bjt = "NPN"
        elif value == "PNP":
            self.bjt = "PNP"
        else:
            print("Please set the BJT type to one of the following: NPN or PNP")

    def bjtCalculations(self):
        # Set transconductance
        self.gm = self.ic / self.vt

        """ Body effect """
        # In effect
        if self.BE is True:
            # Set input resistance
            # AKA base-to-emitter resistance
            self.rpi = self.beta / self.gm

        # Neglected
        if self.BE is False:
            print("Write this")
            self.rpi = 0

        """ Channel length modulation """
        # In effect
        if self.CLM is True:
            # Set output resistance
            if self.bjtType == "PNP":
                self.ro = self.va / self.ic
            if self.bjtType == "NPN":
                self.ro = (self.va - self.vt) / self.ic

            """ Maximum gain """
            # Set open-circuit voltage gain
            if self.va:
                self.uf = self.va / self.vt
            else:
                self.uf = self.gm * self.ro

        # Neglected
        if self.CLM is False:
            """ Maximum gain """
            # Set open-circuit voltage gain
            self.uf = self.gm * self.ro

        """ Capacitance """
        # Emitter-base junction depletion capacitance
        if self.cje0:
            self.cje = 2 * self.cje0

        # Base-charging capacitance
        if self.tau_f:
            self.cb = self.tau_f * self.gm

            # Base-emitter capacitance
            self.cpi = self.cb + self.cje

        # Collector-base junction capacitance
        if self.cu0:
            self.cu = self.cu0 / (1 - ((self.vbc / self.phi0c) ** 0.33))

        # Collector-substrate junction capacitance
        if self.cs0:
            self.cs = self.cs0 / (1 - ((self.vsc / self.phi0s) ** 0.33))

        """ Unity Gain Frequency """
        if self.cje:
            self.ft = (1 / math.pi) * (
                    self.gm / ((self.tau_f * self.gm) + self.cje + self.cu)
            )

        elif self.cu0:
            self.ft = (1 / math.pi) * (
                self.gm / ((self.tau_f * self.gm) + (3 * self.cu0))
            )

        elif self.tau_f:
            self.ft = (1 / math.pi * (
                self.gm / (self.tau_f * self.gm))
            )

    def cbaCalculations(self):
        """Calculations"""
        if self.beta == 0:
            # Set maximum low frequency voltage gain
            self.max_av = (self.rc / self.re)
        else:
            # Set maximum low frequency voltage gain
            self.max_av = (self.rc / self.re)

            # Set small-signal transconductance gain
            self.gm = (self.ic / self.vt)

            # Set output resistance
            """NOTE: Neglecting BWM, set high"""
            self.ro = 10e20

            # Set rpi
            """NOTE: Neglecting BWM"""
            self.rpi = (self.beta / self.gm)

            # Set low frequency input resistance
            self.ri = (
                    ((self.rpi + self.rb) / (self.beta + 1))
                    * (1 + (self.rc / self.ro))
            )

            # Set low frequency output resistance
            self.Ro = self.rc

            # Set low frequency voltage gain
            self.av = (
                    (self.beta * self.Ro) /
                    (self.rb + self.rpi +
                     (self.re * (self.beta + 1))
                     )
            )

    def ccaCalculations(self):
        """Calculations"""
        # Set maximum low frequency voltage gain
        self.max_av = 1

        # Set small-signal transconductance gain
        self.gm = (self.ic / self.vt)

        # Set output resistance
        # """NOTE: Neglecting BWM, set high"""
        # self.ro = 10e20

        # Set rpi
        """NOTE: Neglecting BWM"""
        self.rpi = (self.beta / self.gm)

        # Set low frequency input resistance
        self.ri = self.rpi + (self.beta + 1) * self.re

        # Set low frequency output resistance
        # For RC << Rc
        self.Ro = (
                (self.re ** -1) +
                (((self.rpi + self.rb) / (self.beta + 1)) ** -1)
        )

        # Set low frequency voltage gain
        self.av = (
                ((self.beta + 1) * self.re) /
                (self.rb + self.rpi +
                 (self.re * (self.beta + 1))
                 )
        )

    def ceaCalculations(self):
        """Calculations"""
        # Set maximum low frequency voltage gain
        self.max_av = (- self.rc / self.re)

        # Set small-signal transconductance gain
        self.gm = (self.ic / self.vt)

        # Set rpi
        """NOTE: Neglecting BWM"""
        self.rpi = (self.beta / self.gm)

        # Set low frequency input resistance
        self.ri = (self.rpi + ((self.beta + 1) * self.re))

        # Set output resistance
        if self.va:
            self.ro = (self.va / self.ic)

            # Set low frequency output resistance
            self.Ro = (
                    ((self.rc ** -1) + (
                            (self.ro * (1 + (self.gm * self.re))) ** -1
                    )) ** -1
            )

        elif self.beta:
            self.ro = self.ic / self.vt

            # Set low frequency output resistance
            self.Ro = (
                    ((self.rc ** -1) + (
                            (self.ro * (1 + (self.gm * self.re))) ** -1
                    )) ** -1
            )

        else:
            self.Ro = self.rc

        self.av = (-self.beta * self.Ro) / (
            (self.rb + self.rpi + self.re * (self.beta + 1))
        )

    """ Calculate outputs """
    def findOutputs(self):
        # Check transistor is set
        if self.transistor is not None:
            # Check BJT is set
            if self.bjtType is not None:
                # Check effects are set
                if (self.CLM is not None) & (self.BE is not None):
                    self.bjtCalculations()

                    # Set values if transistor is CBA type
                    if self.transistor == "CBA":
                        self.cbaCalculations()

                    # Set values if transistor is CCA type
                    if self.transistor == "CCA":
                        self.ccaCalculations()

                    # Set values if transistor is CEA type
                    if self.transistor == "CEA":
                        self.ceaCalculations()
                else:
                    print("Error: CLM and BE effects are not set to true/false")
            else:
                print("Error: BJT type is not set")
        else:
            print("Error: Transistor type is not set")


# Set variables
rc = 34.1 * 1e3
re = 0.9 * 1e3
rb = 0.3 * 1e3
beta = 42
ic = 711 * 1e-6
va = None

v_t = 26e-3

# Set variables
variables = [
    rc,
    rb,
    re,
    beta,
    ic,
    va,
    v_t,
]

# Create amplifier class with constants
amp = BjtAmplifier(variables)

# Set effects
amp.switchCLM(True)
amp.switchBE(False)

# Set amplifier
amp.transistorType("CEA")
amp.bjtType("NPN")
amp.findOutputs()


# List of variables to print from class
print_list = [
    "max_av",
    "ri",
    "av"
]

# Print in scientific format
for var in vars(amp):
    for x in print_list:
        if x == var:
            values = getattr(amp, var)
            print(var, " is  {:.2E}".format(values))
