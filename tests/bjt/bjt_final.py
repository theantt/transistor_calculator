import bjt_device_physics.bjt_formulas as bjt

bjt_type = "NPN"
va = 75
ic = 788e-6  # Collector current, Ic (A)

assert bjt.r_o(bjt_type, va, ic, vt) == 95178.0, "Should be 95 kOhm"
