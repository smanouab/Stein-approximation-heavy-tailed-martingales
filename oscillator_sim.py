"""Harmonic-oscillator chain (Jara-Komorowski-Olla): simulation by rejection.
mu is sampled by rejection under the uniform law (density of mu <= 3/2),
p(z,.) = k(z,.) mu(.) by rejection under mu (k <= 6)."""
import numpy as np
from scipy.special import gamma as Gam
pi = np.pi
ALPHA = 1.5

def mu_dens(y): return (4/3)*(1+2*np.cos(pi*y)**2)*np.sin(pi*y)**2
def kfun(z, y):
    return 3*(np.sin(pi*(z+y))**2+np.sin(pi*(z-y))**2)/((1+2*np.cos(pi*z)**2)*(1+2*np.cos(pi*y)**2))
def G(y): return 1/(2*(1+2*np.cos(pi*y)**2)*np.sin(pi*y)**2)
def f(y, a=1.0): return np.sign(y)*np.sqrt(a)*G(y)

def sample_mu(m, rng):
    out = np.empty(m); filled = 0
    while filled < m:
        k = int(1.6*(m-filled))+16
        y = rng.random(k)-0.5
        acc = y[rng.random(k)*1.5 <= mu_dens(y)]
        t = min(len(acc), m-filled); out[filled:filled+t] = acc[:t]; filled += t
    return out

def step(z, rng, M=6.0):
    """One transition from each z (vector) by rejection: proposal mu, bound k <= M."""
    out = np.empty_like(z); todo = np.arange(len(z))
    while len(todo):
        y = sample_mu(len(todo), rng)
        ok = rng.random(len(todo))*M <= kfun(z[todo], y)
        out[todo[ok]] = y[ok]; todo = todo[~ok]
    return out

def I_alpha(a): return pi/(2*Gam(1+a)*np.sin(pi*a/2))
def constants(a=1.0):
    cstar = (4*pi**2/3)*(np.sqrt(a)/(6*pi**2))**1.5
    cbar = ALPHA*cstar                    # Levy weight of the target
    d = 2*cbar*I_alpha(ALPHA)             # E cos(tX) = exp(-d |t|^alpha)
    return cstar, cbar, d

def simulate(n, R, rng, chain=True):
    """Returns n^{-1/alpha} sum_{k<=n} f(Z_k) for R paths (chain, Z_0 ~ mu) or i.i.d. under mu."""
    S = np.zeros(R)
    z = sample_mu(R, rng)
    for _ in range(n):
        z = step(z, rng) if chain else sample_mu(R, rng)
        S += f(z)
    return S*n**(-1/ALPHA)

if __name__ == "__main__":
    import time
    rng = np.random.default_rng(2026)
    yy = np.linspace(-.5, .5, 20001)
    print("max mu density =", mu_dens(yy).max(), "  max k =", kfun(yy[:, None][::50], yy[None, ::50]).max())
    cstar, cbar, d = constants()
    print("c* =", cstar, " cbar =", cbar, " d =", d, " E cos X =", np.exp(-d))
    t = time.time(); S = simulate(100, 20000, rng); print("n=100 R=2e4:", time.time()-t, "s", np.cos(S).mean())
