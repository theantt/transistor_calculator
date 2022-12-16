import bjt_device_physics.bjt_formulas as bjt

# Variable definitions
ic = 954e-6            # Collector current, Ic (A)
vt = 26e-3           # Thermodynamic temperature, Vt (V)
# va = 116     # Early voltage, Va (V)

# Test cases
def test_gm():
    # Variable definitions
    ic = 954e-6  # Collector current, Ic (A)
    assert round(bjt.gm(ic, vt), 3) == 37e-3, "Should be 36.69 mA/V"


def test_un():
    # Variable definitions
    """NOTE: VA IS INFINITE IF BASE-WIDTH OR BODY-EFFECT IS NEGLECTED"""
    va = 116     # Early voltage, Va (V)
    assert round(bjt.un(va, vt), 2) == 4461.54, "Should be 4500 V/V"


def test_rpi():
    # Variable definitions
    """NOTE: VA IS INFINITE IF BASE-WIDTH OR BODY-EFFECT IS NEGLECTED"""
    ic = 286e-6   # Collector current, Ic (A)
    beta = 32     # Beta
    assert bjt.r_pi(ic, beta, vt) == 2909, "Should be 2.91 kOhm"


def test_NPN_ro():
    # Variable definitions
    """NOTE: VA IS INFINITE IF BASE-WIDTH OR BODY-EFFECT IS NEGLECTED"""
    bjt_type = "NPN"
    va = 56
    ic = 523e-6   # Collector current, Ic (A)
    assert bjt.r_o(bjt_type, va, ic, vt) == 107025.0, "Should be 107 kOhm"


def test_PNP_ro():
    # Variable definitions
    """NOTE: VA IS INFINITE IF BASE-WIDTH OR BODY-EFFECT IS NEGLECTED"""
    bjt_type = "PNP"
    va = 75
    ic = 788e-6   # Collector current, Ic (A)
    assert bjt.r_o(bjt_type, va, ic, vt) == 95178.0, "Should be 95 kOhm"

def test_c_pi():
    # What is the base-to-emitter capacitance, Cπ, in fF
    # for an PNP BJT operating in the forward-active region at 27° C
    # with Ic = 140µA? Use: τf = 130psec, Cje0 = 70fF and Vt = kT/q = 26mV.
    ic = 140e-6
    tau_f = 130e-12
    cje0 = 70e-15
    gm = bjt.gm(ic, vt)
    cb = bjt.c_b(tau_f, gm)
    assert bjt.c_pi(cb, cje0) == 8.4e-13, "Should be 840 fF"


def test_c_mu():
    # What is the base-to-collector capacitance, Cµ, in fF
    # for an PNP BJT operating in the forward-active region at 27° C
    # with |Vcb| = 0.2V? Use: Cµ0 = 154fF and φ0 = 0.7V.
    vcb = 0.2
    cmu0 = 154e-15
    phi0 = 0.7
    assert round(bjt.c_mu(cmu0, vcb, phi0), 15) == 1.45e-13, "Should be 145 fF"


def test_u_f():
    # What is the unity gain frequency, Ft, in GHz for an NPN BJT
    # operating in the forward-active region at 27° C with Ic = 411µA?
    # Use: τf = 39psec, Cje0 = Cµ0 = 20fF and Vt = kT/q = 26mV.
    ic = 411e-6
    tauf = 39e-12
    cmu0 = 20e-15

    gm = bjt.gm(ic, vt)

    assert round(bjt.f_t(gm, tauf, cmu0), -8) == 3700000000.0, "Should be 3.7 GHz"


if __name__ == "__main__":
    test_gm()
    test_un()
    test_rpi()
    test_NPN_ro()
    test_NPN_ro()
    test_c_pi()
    test_c_mu()
    test_u_f()

    print("Everything passed")