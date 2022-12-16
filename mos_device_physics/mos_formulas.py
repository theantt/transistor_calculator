import math

"""
Transconductance
NMOS back-gate transconductance
"""
# What is the back-gate transconductance, gmb, in mA/V for an NMOS FET
# operating in saturation with Id = 481µA and Vsb = 2.3V ?
# Use: W/L = 88, k’n = 100μA/V^2, γ = 0.5 V^0.5 and 2φf = 0.6V.


# First find V OV or VON #
def v_on(i_d, k, wl):
    output = math.sqrt(
        (2 * i_d) / (k * wl)
    )
    return output


# Find device transconductance #
def gm_nmos(i_d, v_ov):
    output = (2 * i_d) / v_ov
    return output


# Back-gate #
def gmb_nmos(gamma, gm, two_phi_f, v_sb):
    output = (
            (gamma * gm) / (
            2 * math.sqrt(two_phi_f + v_sb)
    )
    )
    return output


"""
Transconductance
PMOS
"""
# PMOS FET operating in saturation with Id = 224µA ?
# Use: W/L = 59 and k’p = 40μA/V^2.
# Neglect the effects of channel-length modulation and body effect.


def gm_pmos(i_d, w_l, k, v_ov):
    if v_ov == 0:
        output = math.sqrt(
            (2 * k * w_l * i_d)
        )
    elif w_l == 0:
        output = gm_nmos(i_d, v_ov)
    else:
        output = "Error, neither v_ov or w_l is zero"
    return output


"""
Open-Circuit Voltage Gain
PMOS
"""
# What is the open-circuit voltage gain, µf, in V/V for an PMOS FET
# operating in saturation with Id = 757µA and Von = |Vgs-Vt| = 208mV?
# Use: λ = 0.40


def uf_pmos(von, pmos_lambda):
    output = (2 / von) * (1 / pmos_lambda)
    return output




"""Capacitances"""


""""
Gate to Source
Saturation
PMOS
"""
# What is the gate-to-source capacitance, Cgs, in fF for an PMOS FET
# operating in saturation with W = 63µm, L = 0.42µm and
# tox = 80 angstroms?


def cgs_pmos_sat(width, length, e_ox, t_ox):
    output = (
        (2/3) * width * length * (e_ox / t_ox)
    )
    return output


"""
Gate to Source
Triode 
NMOS
"""
# What is the gate-to-source capacitance, Cgs, in fF for
# an NMOS FET operating in triode with W = 27µm, L = 0.11µm
# and tox = 29 angstroms?


def cgs_nmos_triode(w, l, e_ox, t_ox):
    output = (
        (1/2) * w * l * (e_ox / t_ox)
    )
    return output


"""
Unity Gain Frequency
"""
# What is the unity gain frequency, Ft, in GHz for an NMOS FET
# operating in saturation with L = 0.92µm and Von = Vgs-Vt = 200mV?
# Use: µn = 650 cm^2/V-sec.


def unity_frequency(mu, length, von):
    mu_c = mu * (10 ** -4)      # convert mu to the correct unit
    output = (
        1.5 * (mu_c / (2 * math.pi * (length ** 2))) * von
    )
    return output


"""
Output resistance
Drain to source
Saturation
PMOS
"""
# What is the output resistance, rds, in kΩ for an PMOS FET
# operating in saturation with Id = 117µA? Use: λ = 0.56


def rds_pmos_sat(i_d, gamma):
    output = (
        1 / (gamma * i_d)
    )
    return output
