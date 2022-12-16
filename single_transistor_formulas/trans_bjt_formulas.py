import bjt_device_physics.bjt_formulas as bjt
import math

# Set standard constants
v_t = 26e-3


"""Common Emitter Amplifier"""


class CommonEmitterAmplifier:
    def __init__(self, values):
        # Set given constants
        self.rc = values[0]
        self.re = values[1]
        self.rb = values[2]
        self.beta = values[3]
        self.ic = values[4]
        self.va = values[5]
        self.vt = values[6]

        """Calculations"""
        # Set maximum low frequency voltage gain
        self.max_av = (- self.rc / self.re)

        # Set small-signal transconductance gain
        self.gm = (self.ic / self.vt)

        # Set rpi
        """NOTE: Neglecting BWM"""
        self.rpi = (self.beta / self.gm)

        # Set low frequency input resistance
        self.ri = (
            self.rpi + (
                (self.beta + 1) * self.re
            )
        )

        # Set output resistance
        if self.va > 0:
            self.ro = (self.va / self.ic)

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

        # Get variables
        # def get_rc(self):
        #     return self.rc


"""Common Base Amplifier"""
class CommonBaseAmplifier:
    def __init__(self, values):
        # Set given constants
        self.rc = values[0]
        self.re = values[1]
        self.rb = values[2]
        self.beta = values[3]
        self.ic = values[4]
        self.vt = values[5]

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


"""Common Collector Amplifier"""
class CommonCollectorAmplifier:
    def __init__(self, values):
        # Set given constants
        self.rc = values[0]
        self.re = values[1]
        self.rb = values[2]
        self.beta = values[3]
        self.ic = values[4]
        self.vt = values[5]

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
            (((self.rpi + self.rb)/(self.beta + 1)) ** -1)
        )

        # Set low frequency voltage gain
        self.av = (
            ((self.beta + 1) * self.re) /
            (self.rb + self.rpi +
                (self.re * (self.beta + 1))
            )
        )
