import numpy as np


one = np.float32(1.0)
onen = np.float32(-1.0)
w = 10

print(f"{'s':^{w}} {'n':^4} {'zf':^{w}} {'zb':^{w}} {'ef':^{w}} {'ef':^{w}}") # where ^ means "centering"

for s in (2.0, 11.0/3, 5.0, 7.2, 10.0): # Tuple to emphasis this is a list we're not going to change.
    for n in (50, 100, 200, 500, 1000): # Integers because each element is an index.
        z = 0.0
        e = 0.0
        zf = np.float32(0.0) # 32 bits is 4 bytes (float32 is single precision)
        ef = np.float32(0.0)
        for kf in range(1, n+1):
            z = z + 1.0 / kf ** s
            e = e + (-1.0) ** (kf -1) / kf ** s
            zf = zf + one / (kf ** s)
            ef = ef + onen ** (kf - 1) / kf ** s

        zb = np.float32(0.0) 
        eb = np.float32(0.0)
        for kb in range(n, 0, -1):
            zb = zb + one / (kb ** s)
            eb = eb + onen ** (kb - 1) / kb ** s
        # errzf = abs((zf - z) / z)
        errzf = abs((zf.astype(np.float64) - z) / z) # subtraction is going to be done in double precision (float64)
        erref = abs((ef.astype(np.float64) - e) / e)

        errzb = abs((zb.astype(np.float64) - z) / z) 
        erreb = abs((eb.astype(np.float64) - e) / e)
        print(f"{s:>{w}.4f} {n:>4} {errzf:>{w}.2e} {errzb:>{w}.2e} {erref:>{w}.2e} {erreb:>{w}.2e}") # where w represents defined width
    print()
            