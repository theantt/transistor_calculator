import math


""" Common Source  """


class CommonSourceAmplifier:
    def __init__(self, values):
        # Set given constants
        self.rd = values[0]
        self.rs = values[1]
        self.rg = values[2]
        self.wl = values[3]
        self.id = values[4]
        self.vt = values[5]
        self.k = values[6]

        # Calculations
        # Approaches infinity
        self.ri = self.rig = 10E20

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


""" Common Gate  """


class CommonGateAmplifier:
    def __init__(self, values):
        # Set given constants
        self.rd = values[0]
        self.rs = values[1]
        self.rg = values[2]
        self.wl = values[3]
        self.id = values[4]
        self.vt = values[5]
        self.k = values[6]
        self.t_lambda = values[7]
        self.gamma = values[8]
        self.two_phi_f = values[9]
        self.vsb = values[10]

        # Calculations
        # Neglect channel-length modulation

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
        p1 = self.rd ** -1
        p2 = self.ro * (1 + (self.gm+self.gds) * self.rs)
        self.Ro = (
            (p1 + (p2 ** -1)) ** -1
        )

        # Find low frequency voltage gain
        av_num = self.gm * self.rd
        av_denom = 1 + self.gm * self.rs
        self.av = av_num / av_denom

        # # Neglect both
        # # Find on voltage
        # self.von = math.sqrt(
        #     (2 * self.id) / (self.k * self.wl)
        # )
        #
        # # Find device transconductance
        # self.gm = (2 * self.id) / self.von
        #
        # # Find low frequency output resistance
        # self.Ro = self.rd
        #
        # # Find low frequency voltage gain
        # av_num = self.gm * self.rd
        # av_denom = 1 + self.gm * self.rs
        # self.av = av_num / av_denom

""" Common Drain  """


class CommonDrainAmplifier:
    def __init__(self, values):
        # Set given constants
        self.rd = values[0]
        self.rs = values[1]
        self.rg = values[2]
        self.wl = values[3]
        self.id = values[4]
        self.vt = values[5]
        self.k = values[6]

        # Calculations
        # Approaches infinity
        self.ri = self.rig = 10E20

        # Find von
        self.von = math.sqrt(
            (2 * self.id) / (self.k * self.wl)
        )

        # Find gm
        self.gm = (
                (2 * self.id) / self.von
        )

        # Assume R0 = RD
        self.Ris = 1 / self.gm
        self.Ro = ((self.rs ** -1) * (self.Ris ** -1)) ** -1
        self.max_av = (self.rd / self.rs)

        # Find av
        self.av = (
            (self.gm * self.rd) / (
                (1 + self.gm * self.rs)
            )
        )