"""Figure for the oscillator chain: histogram of M_n (n=1000) vs the stable limit,
and |Delta_n| for the chain (Monte Carlo) and the i.i.d. benchmark (exact)."""
import json, os, sys
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import levy_stable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from oscillator_sim import constants, ALPHA
plt.rcParams.update({"font.family": "serif", "font.size": 8.5, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True, "grid.color": "#e4e3df",
                     "legend.frameon": False, "savefig.bbox": "tight"})
here = os.path.dirname(os.path.abspath(__file__))
cstar, cbar, d = constants()
scale = d**(1/ALPHA)
S = np.load(os.path.join(here, "osc_sample_n1000.npy"))
res = json.load(open(os.path.join(here, "osc_results.json")))
iid = {100: -0.011406, 1000: -0.005418, 10000: -0.002546}   # exact, oscillator_exact.py
fig, ax = plt.subplots(1, 2, figsize=(6.4, 2.55))
bins = np.linspace(-1.5, 1.5, 97); w = bins[1]-bins[0]
cnt, _ = np.histogram(S, bins=bins)
ax[0].bar(bins[:-1], cnt/(len(S)*w), width=0.92*w, align="edge", color="#2a78d6", alpha=0.45, lw=0,
          label=r"$n^{-2/3}\sum_{k\leq n} f(Z_k)$, $n=1000$")
xx = np.linspace(-1.5, 1.5, 400)
ax[0].plot(xx, levy_stable.pdf(xx, ALPHA, 0, scale=scale), color="k", lw=1.2, label=r"limit $S(3/2,0,\gamma_{\bar c},0;0)$")
ax[0].set(xlabel=r"$x$", ylabel="density", title="Oscillator chain, $Z_0\\sim\\mu$")
ax[0].set_ylim(0, 1.55); ax[0].legend(loc="upper left", fontsize=6.8)
n = np.array([r["n"] for r in res]); dch = np.array([abs(r["delta"]) for r in res]); se = np.array([r["se"] for r in res])
ax[1].errorbar(n, dch, yerr=2*se, fmt="o-", color="#eb6834", ms=4, lw=1.1, capsize=2, label="chain (Monte Carlo, $\\pm2$ s.e.)")
ax[1].plot(list(iid), [abs(v) for v in iid.values()], "s--", color="#1baf7a", ms=4, lw=1.0, label="i.i.d. under $\\mu$ (exact)")
nn = np.logspace(1.9, 4.1, 50); ax[1].plot(nn, 0.055*nn**(-1/3), ":", color="k", lw=0.9, label=r"slope $-1/3$")
ax[1].set(xscale="log", yscale="log", xlabel=r"$n$", ylabel=r"$|\mathbb{E}\cos M_n-\mathbb{E}\cos X|$", title=r"Rate $n^{-1/3}$")
ax[1].legend(loc="lower left", fontsize=6.8)
fig.tight_layout(w_pad=1.5)
out = os.path.join(here, "..", "figures", "fig_oscillator")
fig.savefig(out+".pdf"); fig.savefig(out+".png", dpi=300)
print("ok", scale)
