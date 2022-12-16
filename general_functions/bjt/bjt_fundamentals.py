import math


# Source current in forward-active (a is the emitter area)
def i_source(q, a, d_n, n_p0, w_b):
    return (q * a * d_n * n_p0) / w_b


# Collector current in forward-active
def ic(i_s, v_be, v_t, v_a, v_ce, beta_f, i_b):
    output = i_s * (math.e ** (v_be/v_t))
    # Include early voltage
    if v_a is not None:
        output = i_s * (math.e ** (v_be/v_t)) * (1 + v_ce/v_a)
    elif i_b and beta_f is not None:
        output = beta_f * i_b
    return output


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
def r_o(bjt_type, v_a, i_c, v_t):
    if bjt_type == 'NPN':
        return round(((v_a - v_t) / i_c), 0)
    if bjt_type == 'PNP':
        output = round(v_a / i_c, 0)
        return output


# C_b (Base-charging capacitance)
def c_b(tau_f, g_m):
    return tau_f * g_m


# C_pi (Base-emitter capacitance)
def c_pi(c_b, c_je0):
    return c_b + (2 * c_je0)


# C_mu (Collector-base junction capacitance)
def c_mu(c_mu0, v_cb, phi_0c):
    return c_mu0 / (((1 + abs(v_cb)) ** 0.33) - (phi_0c * (10 ** -15)))


# C_cs (Collector-substrate junction capacitance)
def c_cs(c_cs0, v_cs, phi_0s):
    return c_cs0 / (((1 + abs(v_cs)) ** 0.33) - (phi_0s * (10 ** -15)))


# f_T (Transition frequency)
def f_T(g_m, tau_f, c_mu0):
    return (1 / (2 * math.pi)) * (g_m / ((tau_f * g_m) + 3 * c_mu0))


# tau_T (Effective transit time)
def tau_T(f_T):
    return 1 / (2 * math.pi * f_T)


# mu_f (Maximum gain, small-signal forward-active)
def max_small_signal_gain(g_m, r_o, v_a, v_t):
    if g_m and r_o:
        output = g_m * r_o
        return output
    elif v_a and v_t:
        output = v_a / v_t
        return output
