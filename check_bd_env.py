"""Birth-death environment model X_k = eps_k + b(Z_{k-1}) zeta_k, reflected walk p,q,
b = B 1{z>=1}; check |Delta_n|/n^{-(2-a)/a} -> (1/2) e^{-d_a} B^2 rho."""
import numpy as np, time
from scipy.special import gamma as G
def I(a): return np.pi/(2*G(1+a)*np.sin(np.pi*a/2))
rng=np.random.default_rng(7)
def run(a,n,R,p=0.3,q=0.5,B=1.0):
    rho=p/q
    Z=rng.geometric(1-rho,R)-1            # stationary law mu(x)=(1-rho) rho^x
    A=np.zeros(R); Bs=np.zeros(R)
    for k in range(n):
        b=B*(Z>=1)
        eps=rng.choice([-1.,1.],R)*rng.random(R)**(-1/a)
        zeta=rng.choice([-1.,1.],R)
        A+=eps; Bs+=b*zeta
        u=rng.random(R)
        up=u<p; down=(u>=p)&(u<p+q)&(Z>0)
        Z=Z+up-down
    s=n**(-1/a); A*=s; Bs*=s
    D=np.cos(A+Bs)-np.cos(A)+np.sin(A)*Bs
    r=n**(-(2-a)/a)
    return abs(D.mean())/r, D.std()/np.sqrt(R)/r, 0.5*np.exp(-a*I(a))*B**2*rho
for a in [1.4,1.5]:
    for n,R in [(100,200000),(1000,100000)]:
        t=time.time(); m,se,lim=run(a,n,R)
        print(f"alpha={a} n={n}: ratio={m:.5f} +- {se:.5f}   limit={lim:.5f}   ({time.time()-t:.0f}s)")
