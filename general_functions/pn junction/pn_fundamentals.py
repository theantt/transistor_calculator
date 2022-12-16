""" PN Junction Fundamentals """
# Thermal voltage
v_t = 26e-3


# Total depletion region
def depletion_width(epsilon, phi_0, v_r, q, n_a, n_d):
    # width of depletion region on p-type side
    w1 = math.sqrt(
        (2 * epsilon * (phi_0 + v_r)) / (q * n_a * (1 + n_a / n_d))
    )
    # width of depletion region on n-_type side
    w2 = math.sqrt(
        (2 * epsilon * (phi_0 + v_r)) / (q * n_d * (1 + n_a / n_d))
    )
    w_dep = w1 + w2

    return w_dep


# Calculate the built-in potential
def built_in_potential(v_t, n_a, n_d, n_i):
    x = (n_a * n_d) / (n_i ** 2)
    phi_0 = v_t * math.log(x)
    return phi_0


def junction_capacitance(cj0, m, v_d, phi_0):
    cj = cj0 / ((1 - (v_d / phi_0)) ** (1/m))
    return cj


def junction_current(i_s, v_d, v_t):
    i = i_s * ((math.e ** (v_d/v_t)) - 1)
    return i

