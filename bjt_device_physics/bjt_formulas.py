import math


# Transconductance (small-signal forward-active)
def gm(i_c, v_t):
    return i_c / v_t


# Open circuit voltage gain
def un(v_a, v_t):
    return v_a / v_t


# r_pi (Input or base-to-emitter resistance)
def r_pi(i_c, beta, v_t):
    return round(v_t / (i_c / beta), 0)


# r_o (Output or collector-to-emitter resistance)
def r_o(type, v_a, i_c, v_t):
    if type == 'NPN':
        return round(((v_a - v_t) / i_c), 0)
    if type == 'PNP':
        output = round(v_a / i_c, 0)
        return output


# C_b (Base-charging capacitance)
def c_b(tau_f, g_m):
    return tau_f * g_m


# C_pi (Base-emitter capacitance)
def c_pi(c_b, c_je0):
    return c_b + (2 * c_je0)


# C_mu (Collector-base junction capacitance)
def c_mu(c_mu0, v_cb, phi_0):
    return c_mu0 / (((1 + abs(v_cb)) ** 0.33) - (phi_0 * (10 ** -15)))


# u_f (Unity gain frequency)
def f_t(g_m, tau_f, c_mu0):
    return (1 / (2 * math.pi)) * (g_m / ((tau_f * g_m) + 3 * c_mu0))
