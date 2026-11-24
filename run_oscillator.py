import numpy as np, time, json, sys
sys.path.insert(0, "code")
from oscillator_sim import simulate, constants, ALPHA
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
cstar, cbar, d = constants()
res = []
for n, R in [(100, 200000), (1000, 100000), (10000, 20000)]:
    t = time.time()
    S = simulate(n, R, rng)
    c = np.cos(S)
    res.append(dict(n=n, R=R, Ecos=float(c.mean()), se=float(c.std()/np.sqrt(R)),
                    delta=float(c.mean()-np.exp(-d)), secs=time.time()-t))
    print(res[-1], flush=True)
    if n == 1000:
        np.save("code/osc_sample_n1000.npy", S[:100000])
json.dump(res, open("code/osc_results.json", "w"), indent=1)
