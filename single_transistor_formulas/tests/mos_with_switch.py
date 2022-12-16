import math


class MosAmplifier:
    def __init__(self, vals):
        # Set given constants
        self.rd = vals[0]
        self.rs = vals[1]
        self.rg = vals[2]
        self.wl = vals[3]
        self.id = vals[4]
        self.vt = vals[5]
        self.k = vals[6]
        self.t_lambda = vals[7]

        """ Initialize transistor options"""
        # Set effects
        # Ignore effects of CLM and BE
        self.CLM = None
        self.BE = None

        # Set transistor
        self.transistor = None
        self.mos = None

        # Set variables to be defined in functions later

        """ Basic MOS """
        # Small-signal forward active
        self.gm = None
        self.rpi = None
        self.ro = None
        self.von = None
        self.gds = None

        """ Single MOS Transistor """
        self.ri = None
        self.rig = None
        self.ris = None
        self.max_av = None
        self.Ro = None
        self.av = None

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
        if value == "CS":
            self.transistor = "CS"
        elif value == "CG":
            self.transistor = "CG"
        elif value == "CD":
            self.transistor = "CD"
        else:
            print("Please set the transistor type to one of the following: CBA, CCA, or CEA")

    def mosType(self, value):
        if value == "NMOS":
            self.mos = "NMOS"
        elif value == "PMOS":
            self.mos = "PMOS"
        else:
            print("Please set the MOS type to one of the following: NMOS or PMOS")

    def cdCalculations(self):
        """Calculations"""
        # Calculations
        if self.CLM == 0 and self.BE == 0:
            # Find on voltage
            self.von = math.sqrt(
                (2 * self.id) / (self.k * self.wl)
            )

            # Find transconductance
            self.gm = (
                    (2 * self.id) / self.von
            )

            # Find av
            self.av = (self.gm * self.rs) / (1 + self.gm * self.rs)

            self.max_av = 1

        # if self.CLM == 1 and self.BE == 0:
        #     print("test")
        #     # Find von
        #     self.von = math.sqrt(
        #         (2 * self.id) / (self.k * self.wl)
        #     )
        #     # Find transconductance
        #     self.gm = (
        #             (2 * self.id) / self.von
        #     )
        #     # Find input resistance Ris
        #     self.ris = (1 / self.gm)
        #
        #     # Find output resistance Ro
        #     self.Ro = ((self.rs ** -1) + (self.ris ** -1)) ** -1

    def cgCalculations(self):
        # Calculations
        # Neglect channel-length modulation

        if self.CLM == 1 and self.BE == 0:
            # Neglect body effect
            # Find on voltage
            self.von = math.sqrt(
                (2 * self.id) / (self.k * self.wl)
            )

            # Find device transconductance
            self.gm = (2 * self.id) / self.von

            # Find output resistance
            self.ro = (
                    1 / (self.t_lambda * self.id)
            )

            # Find ds transconductance
            self.gds = 1 / self.ro

            # Find low frequency output resistance
            self.Ro = (
                    ((self.rd ** -1) + ((self.ro * (1 + (self.gm + self.gds) * self.rs)) ** -1)) ** -1
            )

            # Find low frequency voltage gain
            av_num = self.gm * self.rd
            av_denom = 1 + self.gm * self.rs
            self.av = av_num / av_denom

        if self.CLM == 0 and self.BE == 0:
            # Neglect both
            # Find on voltage
            self.von = math.sqrt(
                (2 * self.id) / (self.k * self.wl)
            )

            # Find device transconductance
            self.gm = (2 * self.id) / self.von

            # Find low frequency output resistance
            self.Ro = self.rd

            # Find low frequency voltage gain
            self.av = (self.gm * self.rd) / (1 + self.gm * self.rs)

    def csCalculations(self):
        # Calculations
        # Approaches infinity
        self.ri = 10E20

        # Find von
        self.von = math.sqrt(
            (2 * self.id) / (self.k * self.wl)
        )

        # Find gm
        self.gm = (
                (2 * self.id) / self.von
        )

        # Assume R0 = RD
        self.Ro = self.rd
        self.max_av = (- self.rd / self.rs)

        # Find av
        self.av = (
                (- self.gm * self.rd) / (
            (1 + self.gm * self.rs)
        )
        )

    """ Calculate outputs """
    def findOutputs(self):
        # Check transistor is set
        if self.transistor is not None:
            # Check MOS is set
            if self.mosType is not None:
                # Check effects are set
                if (self.CLM is not None) & (self.BE is not None):

                    # Set values if transistor is CS type
                    if self.transistor == "CS":
                        self.csCalculations()

                    # Set values if transistor is CG type
                    if self.transistor == "CG":
                        self.cgCalculations()

                    # Set values if transistor is CD type
                    if self.transistor == "CD":
                        self.cdCalculations()
                else:
                    print("Error: CLM and BE effects are not set to true/false")
            else:
                print("Error: MOS type is not set")
        else:
            print("Error: Transistor type is not set")


""" Main function """
# Set standard constants
v_t = 26e-3
k_n = 100e-6
k_p = 40e-6
vt_n = 0.5
vt_p = -0.5

# Variables given as arguments
rd = 15.5 * 1e3
rs = 3.0 * 1e3
rg = 3.9 * 1e3
wl = 21
i_d = 879 * 1e-6
vt = v_t        # vtn or vtp
k = k_p
t_lambda = 0

# Set variables
variables = [
    rd,  # rd
    rs,  # rs
    rg,  # rg
    wl,  # wl
    i_d,  # id
    vt,  # vtn or vtp
    k,  # k
    t_lambda,  # lambda
]

# Create amplifier class with constants
amp = MosAmplifier(variables)

# Set effects
amp.switchCLM(True)
amp.switchBE(False)

# Set amplifier
amp.transistorType("CD")
amp.mosType("PMOS")
amp.findOutputs()


# List of variables to print from class
print_list = [
    "gm",
    "av"
]

# Print in scientific format
for var in vars(amp):
    for x in print_list:
        if x == var:
            values = getattr(amp, var)
            print(var, " is  {:.2E}".format(values))
