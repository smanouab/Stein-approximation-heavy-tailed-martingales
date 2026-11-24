# Stein-approximation-heavy-tailed-martingales
Non-asymptotic bounds for stable approximation of heavy-tailed martingale differences and Markov chains using Stein’s method!

# 🔬 Stable Approximation of Heavy-Tailed Martingale Differences and Markov Chains via Stein’s Method

<p align="center">
  <strong>Non-asymptotic bounds · Stable limit theorems · Dependence · Stein's method</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Mathematics-Probability-blue" />
  <img src="https://img.shields.io/badge/Method-Stein's%20Method-purple" />
  <img src="https://img.shields.io/badge/Limit%20Law-%CE%B1--stable-orange" />
  <img src="https://img.shields.io/badge/Status-Research%20Project-green" />
</p>

---

## 📖 Overview

This repository contains the research materials associated with the paper:

**Stable Approximation of Sums of Heavy-Tailed Martingale Differences and Markov Chains via Stein’s Method**

**Authors:**  
- Solym M. Manou-Abi  
- Abdoul F. Ouedraogo  

The paper investigates quantitative stable approximation for sums of heavy-tailed random variables in dependent settings. While stable approximation is well understood for independent summands, obtaining explicit error bounds under dependence remains a challenging problem.

We develop a Stein's method and Lindeberg-principle approach to derive explicit, non-asymptotic error bounds for normalized sums of heavy-tailed martingale differences.

## 🎯 Main Contributions

The paper develops several complementary results:

- **Non-asymptotic stable approximation:** Explicit error bounds for normalized sums of heavy-tailed martingale differences.
- **Conditional tail assumption:** A main bound under a conditional tail condition, recovering the rate known for independent summands.
- **General dependence bound:** A second bound applicable to integrable martingale difference sequences, which quantifies the contribution of dependence.
- **Markov chain applications:** An extension to state-dependent conditional tails in ergodic Markov chains, including a model arising from a system of harmonic oscillators.
- **Sharpness and numerical evidence:** Theoretical and numerical investigations of the relevance of the derived rates and the role of the conditional tail assumption.
- **Multidimensional perspective:** Discussion of a possible extension to higher-dimensional stable approximation.

## 🧮 Mathematical Framework

The main objects of study are normalized partial sums of heavy-tailed martingale differences:

\[
S_n = \sum_{k=1}^{n} X_k,
\]

where \((X_k)_{k\geq 1}\) is a sequence of martingale differences with respect to a filtration \((\mathcal{F}_k)_{k\geq 0}\).

Under suitable assumptions, the normalized sums are approximated by an \(\alpha\)-stable distribution, with \(\alpha\in(0,2)\).

Our approach combines:

- Stein's method for stable distributions;
- The Lindeberg replacement principle;
- Conditional tail estimates;
- Smooth Wasserstein-type probability metrics;
- Martingale and Markov chain techniques.

The objective is to understand how dependence affects the quality of stable approximation and under which assumptions the independent-summand rate can still be recovered.

## 🧪 Applications and Numerical Experiments

The theoretical results are illustrated through several examples:

| Application | Description |
|---|---|
| Linear processes | Stable approximation in dependent linear structures |
| Markov chains | Additive functionals and state-dependent conditional tails |
| Harmonic oscillators | An ergodic Markov chain model |
| Numerical experiments | Illustration of approximation errors and convergence rates |

Numerical experiments are intended to complement the theoretical analysis and provide insight into the behavior of the bounds.

## 📂 Repository Structure

The repository is organized as follows:

```text
stable-approximation-heavy-tailed-martingales/
│
├── README.md
│
├── paper/
│   ├── main.tex
│   ├── references.bib
│   └── figures/
│
├── code/
│   ├── simulations/
│   ├── linear_processes/
│   ├── markov_chains/
│   └── harmonic_oscillators/
│
├── results/
│   ├── figures/
│   └── numerical_results/
│
├── LICENSE
└── .gitignore
```

*The structure will be updated as the manuscript, codes and numerical materials are added.*

## ⚙️ Reproducibility

The numerical experiments will be accompanied by scripts and documentation whenever possible.

The computational materials are intended to facilitate:

- Reproduction of the numerical experiments;
- Exploration of the approximation errors;
- Investigation of the impact of dependence;
- Comparison between theoretical bounds and empirical behavior.

Specific software requirements and execution instructions will be provided in the corresponding folders.

## 📚 Keywords

`Stein's method` · `Lindeberg principle` · `Stable distributions` · `Heavy-tailed random variables` · `Martingale differences` · `Markov chains` · `Conditional tails` · `Stable approximation` · `Wasserstein distance` · `Rates of convergence`

## 👥 Authors

**Solym M. Manou-Abi**  
Applied Mathematics and Data Science  
Université de Poitiers, France  
Laboratoire de Mathématiques et Applications (LMA), UMR CNRS 7348

**Abdoul F. Ouedraogo**

## 📄 Citation

If you use this work in your research, please cite the corresponding paper.

A BibTeX entry will be added once the publication details are available.

```bibtex
@unpublished{ManouAbiOuedraogoStableApproximation,
  author = {Manou-Abi, Solym M. and Ouedraogo, Abdoul F.},
  title = {Stable Approximation of Sums of Heavy-Tailed Martingale Differences
           and Markov Chains via Stein's Method},
  note = {Preprint}
}
```

## 📜 License

The source code is distributed under the MIT License, unless otherwise specified. The manuscript and other research materials remain subject to their respective copyright and licensing conditions.

---

<p align="center">
  <strong>📊 Probability · Heavy Tails · Dependence · Stable Laws</strong>
  <br/>
  Advancing quantitative limit theory for dependent heavy-tailed systems.
</p>
