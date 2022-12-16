import math

"""Large signal MOS"""


# c_ox (Capacitance per unit area)
def calc_c_ox(t_ox):
    epsilon_r = 3.9  # SiO2 permittivity
    epsilon_0 = 8.854e-12  # F/m
    e_ox = epsilon_r * epsilon_0
    return e_ox / t_ox


# c_gate (Gate capacitance)
def calc_c_gate(w, l, c_ox):
    return w * l * c_ox


"""NOTE: Triode"""


def calc_v_on(v_gs, v_t, k, i_d, wl):
    if v_gs is not None:
        output = v_gs - v_t
        return output
    elif k and i_d and wl is not None:
        output = math.sqrt((2 * i_d) / (k * wl))
        return output


# i_d (Drain current in triode or saturation)
def calc_i_d(k, wl, v_on, v_ds, x, t_lambda):
    if x == "triode":
        output = (k / 2) * wl * (2 * v_on * v_ds - (v_ds ** 2))
        return output
    if x == "saturation":
        output = (k / 2) * wl * (v_on ** 2) * (1 + t_lambda * v_ds)
        return output


# r_ds ("On resistance" in triode)
def calc_r_ds(k, wl, v_on):
    return (k * wl * v_on) ** -1


""" Small signal MOS in saturation """


# g_m (Transconductance)
def calc_g_m(k, wl, v_on, i_d):
    if wl and i_d is not None:
        return math.sqrt(2 * k * wl * i_d)
    elif v_on is not None:
        if i_d is None:
            return k * wl * v_on
        else:
            return (2 * i_d) / v_on


# g_mb (Back gate transconductance)
def calc_g_mb(g_m, gamma, two_phi_f, v_sb):
    if gamma is not None:
        x = (gamma / (2 * math.sqrt(two_phi_f + v_sb))) * g_m
        return x
    else:
        return 0


# r_ds, r_o (Output resistance)
def r_ds(r_o, t_lambda, i_d):
    if r_o is not None:
        return r_o
    else:
        return 1 / (t_lambda * i_d)

# mu_f (Maximum voltage gain)
def max_voltage_gain(g_m, r_o, t_lambda, v_on, v_a):
    if g_m and r_o is not None:
        return g_m * r_o
    elif t_lambda is not None:
        return (1 / t_lambda) * (2 / v_on)
    elif v_a is not None:
        return (2 * v_a) / v_on


""" MOS capacitances """


# c_gs
def calc_c_gs(c_ox, w, l, x):
    if x == "saturation":
        return (2/3) * w * l * c_ox
    if x == "triode":
        return (1/2) * w * l * c_ox


# c_sb (Source-body depletion capacitance)
def calc_c_csb(c_sb0, v_sb, phi_0):
    return c_sb0 / ((1 + (v_sb / phi_0)) ** 0.33)


# c_db (Drain-body depletion capacitance)
def calc_c_cdb(c_db0, v_db, phi_0):
    return c_db0 / ((1 + (v_db / phi_0)) ** 0.33)


# f_T (Transition frequency)
def calc_f_T(g_m, c_gs, c_gb, c_gd):
    return (1 / (2 * math.pi)) * (g_m / (c_gs * c_gb * c_gd))


