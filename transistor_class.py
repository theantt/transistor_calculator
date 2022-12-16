class MyTransistor:
    def __init__(self, t_type, variables):
        self.type = t_type[0]
        self.config = t_type[1]

        # Given constants
        self.ie = variables[0]
        self.ic = variables[1]
        self.ib = variables[2]

        # Calculated or given inputs
        self.alpha = variables[3]
        self.beta_f = variables[4]

        # Calculated input
        self.av = None

    def typeBJT(self):
        if self.type = "BJT":
            





# Set defined variables
ie = None
ic = None
ib = None
alpha = None
beta_f = None

# Set defined configuration
transistor = "BJT"
amplifier = "CB"

variables = [
    ie,         # emitter current
    ic,         # collector current
    ib,         # base current
    alpha,      # current gain ic/ie
    beta_f,     # forward current gain (ic/ib)
]

transistor_type = [
    transistor,
    amplifier,
]