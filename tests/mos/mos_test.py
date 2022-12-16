import mos_device_physics.mos_formulas as mos

# Variable definitions
kn = 100e-6
kp = 40e-6
eox = 3.9 * 8.854e-12

# Test cases
def test_v_on():
    # Variable definitions
    id = 481e-6
    wl = 88

    assert round(mos.v_on(id, kn, wl), 2) == 0.33, "Should be 0.33 V"


def test_gm_nmos():
    # Variable definitions
    id = 481e-6
    wl = 88
    von = mos.v_on(id, kn, wl)

    output = round(mos.gm_nmos(id, von), 4)
    assert output == 0.0029, "Should be 0.0029 A/V"


def test_gmb_nmos():
    # Variable definitions
    id = 481e-6
    wl = 88
    gamma = 0.5
    two_phi_f = 0.6
    vsb = 2.3

    von = mos.v_on(id, kn, wl)
    gm = mos.gm_nmos(id, von)

    output = round(mos.gmb_nmos(gamma, gm, two_phi_f, vsb), 6)
    assert output == 0.000427, "Should be 0.427 mA/V"


def test_gm_pmos():
    """Variation: No V_on given"""
    # Variable definitions
    # id = 224e-6
    # wl = 59
    # von = 0
    #
    # output = round(mos.gm_pmos(id, wl, kp, von), 6)
    #assert output == 0.001028, "Should be 1.028 mA/V"

    """Variation: With V_on given"""
    # Variable definitions
    id = 870e-6
    wl = 0
    von = 147e-3

    output = round(mos.gm_pmos(id, wl, kp, von), 4)
    assert output == 0.0118, "Should be 11.8 mA/V"


def test_uf_pmos():
    # Variable definitions
    von = 208e-3
    x_lambda = 0.4

    output = round(mos.uf_pmos(von, x_lambda), 2)
    assert output == 24.04, "Should be 24.04 V/V"


def test_cgs_pmos_sat():
    # Variable definitions
    w = 63e-6
    l = 0.42e-6
    tox = 80e-10

    output = round(mos.cgs_pmos_sat(w, l, eox, tox), 16)
    assert output == 7.61e-14, "Should be 76.1 fF"


def test_cgs_nmos_triode():
    # Variable definitions
    w = 27e-6
    l = 0.11e-6
    tox = 29e-10

    output = round(mos.cgs_nmos_triode(w, l, eox, tox), 16)
    assert output == 1.77e-14, "Should be 17.7 fF"


def test_unity_frequency_nmos():
    mu_n = 650
    length = 0.92e-6
    von = 200e-3

    output = round(mos.unity_frequency(mu_n, length, von), -8)
    assert output == 3700000000, "Should be 3.7 GHz"


def test_unity_frequency_pmos():
    mu_p = 250
    length = 0.15e-6
    von = 238e-3

    output = round(mos.unity_frequency(mu_p, length, von), -8)
    assert output == 63100000000, "Should be 63.1 GHz"


def test_rds():
    # Variable definitions
    id = 117e-6
    gamma = 0.56

    output = round(mos.rds_pmos_sat(id, gamma), -1)
    assert output == 15260, "Should be 15.26 kOhm"


if __name__ == "__main__":
    # Finding NMOS back-gate transconductance
    test_v_on()
    test_gm_nmos()
    test_gmb_nmos()

    # PMOS transconductance
    test_gm_pmos()

    # Unity gain of PMOS
    test_uf_pmos()

    # Gate to source capacitances
    test_cgs_pmos_sat()
    test_cgs_nmos_triode()

    # Unity gain frequency
    test_unity_frequency_nmos()
    test_unity_frequency_pmos()

    # Output resistance
    test_rds()


    print("Everything passed")
