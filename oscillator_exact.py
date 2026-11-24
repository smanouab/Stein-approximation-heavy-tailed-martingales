"""Exact i.i.d. benchmark and uniform conditional-tail remainder for the oscillator chain."""
import numpy as np, sys
from scipy.integrate import quad
from scipy.optimize import brentq
sys.path.insert(0, "code")
from oscillator_sim import mu_dens, kfun, G, f, constants, ALPHA
cstar, cbar, d = constants()
# 1) i.i.d.: E cos(t f(Z)) under mu, f odd -> E cos(t f) = 2 int_0^{1/2} cos(t f(y)) mu(y) dy
def phi(t):
    g = lambda y: (1-np.cos(t*f(y)))*mu_dens(y)
    # integrate carefully near 0 where f blows up: split at points
    pts = [0, 1e-6, 1e-4, 1e-3, 1e-2, 0.05, 0.5]
    s = sum(quad(g, pts[i], pts[i+1], limit=2000, epsabs=1e-15, epsrel=1e-12)[0] for i in range(len(pts)-1))
    return 1-2*s
print("i.i.d. benchmark: (E cos A_n - e^{-d}) / n^{-1/3}")
for n in [1e2, 1e3, 1e4, 1e6]:
    val = np.exp(n*np.log(phi(n**(-1/ALPHA))))
    print(f"  n={n:g}: E cos A_n={val:.6f}  delta={val-np.exp(-d):.6f}  ratio={(val-np.exp(-d))*n**(1/3):.4f}")
# 2) uniform remainder: sup_z |P_z(f(Z_1)>x) - k(z,0) c* x^{-3/2}| x^{5/2}
y_of = lambda x: brentq(lambda y: G(y)-x, 1e-12, 0.5)
zs = np.linspace(-0.5, 0.5, 41)
for x in [1e1, 1e2, 1e3, 1e4]:
    y0 = y_of(x)
    errs = [abs(quad(lambda y: kfun(z, y)*mu_dens(y), 0, y0, epsabs=1e-18)[0] - kfun(z, 0)*cstar*x**-1.5)*x**2.5 for z in zs]
    print(f"x={x:g}: sup_z |remainder| * x^(5/2) = {max(errs):.4f}")
