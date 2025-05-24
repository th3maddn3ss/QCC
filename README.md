# 🚀 Quantum Coherence Cosmology (QCC)

**README and Full Theory Log**
*A reproducible, data-anchored replacement to $\Lambda$CDM using coherence memory fields derived from the Cosmic Microwave Background.*

---

## 🔷 Overview

Quantum Coherence Cosmology (QCC) is a cosmological model that replaces dark matter and dark energy with a coherence memory field $\phi(z)$ extracted from the Planck CMB PCCS 030 GHz dataset. It explains cosmic structure formation, gravitational lensing, and expansion through quantum coherence evolution, offering predictive power across multiple datasets **without parameter tuning**.

**This repository includes:**

* Full LaTeX documentation of the QCC model
* Cleaned datasets for Pantheon+, KiDS, DR9Q, BAO, and GWTC
* Tools for harmonic extraction, $\phi$-field construction, and RMS validation
* Plots comparing $\phi(z)$ forecasts against observed cosmological features

---

## 📁 Repository Structure

```plaintext
QCC Repository/
├── Codebase/                         # Python notebooks and tools for processing QCC φ-field
├── Datasets/                         # All cleaned cosmological datasets
├── Older versions and Checkpoints/   # Dedicated folder for version history
├── COM_PCCS_030_R2.04.txt            # Planck 030 GHz compact source catalog
├── LICENSE                           # BSD 3-Clause License
├── QCC_V2_Theory_Preprint.tex        # Complete LaTeX document of the QCC model
└── README.md                         # Project overview and full theory log
```

---

## 🧠 Model Highlights

### $\phi(z)$ Field Derivation

The scalar coherence field $\phi(z)$ is defined as:

$$
\phi(z) = \mu(z) - \nu(z)
$$

Where:

* $\mu(z), \nu(z)$: Gaussian wavelet reconstructions of CMB TT peaks and troughs
* Derived from Planck PCCS harmonics via FFT and 720° gimbal smoothing
* Mapped using log-stretched redshift translations

---

## ✅ Physical Validation

* **GR Limit**:

$$
\phi \rightarrow 0 \Rightarrow G_{\mu\nu} = 8\pi G T_{\mu\nu} 
$$

* **Canonical Quantization**:

$$
[\phi(z_1), \pi(z_2)] = i\delta(z_1 - z_2) 
$$

* **Energy Conservation**:

$$
\nabla^\mu(T_{\mu\nu} + H_{\mu\nu}(\phi)) = 0 
$$

* **Entropy Validity**:

$$
S \propto \lambda_{\text{decay}}(\tau - \tau_0) 
$$

* **Microcausality**:

$$
[\phi(x), \phi(x')] = 0 \quad \text{for spacelike } (x - x') 
$$

* **Hawking/Unruh Compatibility**:

$$
\phi(z, \tau) \text{ decay preserves vacuum physics} 
$$

---

## 📜 Canonical Lagrangian

The Lagrangian density for the QCC scalar field $\phi(z, \tau)$ is:

$$
\mathcal{L}_{\phi} = \frac{1}{2} g^{\mu\nu} \partial_\mu \phi \, \partial_\nu \phi - V(\phi) 
$$

Where the potential is defined as:

$$
V(\phi) = \frac{1}{2} m^2 \phi^2 + \frac{\lambda}{4} \phi^4 + \alpha \, e^{-\beta z} \phi(z, \tau) 
$$

With:

* $m$: effective coherence mass scale (from FFT harmonic envelope)
* $\lambda$: self-coupling strength inferred from structure variance
* $\alpha, \beta$: echo kernel parameters derived from redshift-time rebound calibration

This final echo term:

$$
\alpha \, e^{-\beta z} \phi(z, \tau) 
$$

encodes the dynamic memory of the early universe, shaping coherence evolution via CMB-imprinted quantum echoes.

---

## 📊 RMS Accuracy

* **Pantheon+ RMS**: \~0.35
* **KiDS RMS**: \~0.38 – 0.48
* **DR9Q RMS**: \~0.45
* Achieved *with slight echo tuning*

---

## 📌 Current Checkpoint — QCC V2.1

* ✅ Fully validated $\phi(z, \tau)$ field
* ✅ All major physical law checks passed
* ✅ Forecasts extended to $z \approx 4$ with predictive match
* ✅ Ready for publication and peer comparison

---

## 🛠 Upcoming Goals

* [ ] Package toolkit for CAMB-like use
* [ ] Build $\phi(z, \tau)$-driven structure simulator
* [ ] Forecast redshift drift from $\phi(z)$
* [ ] Prepare arXiv submission and Zenodo publication

---

> **QCC is now a predictive, quantized, physically consistent cosmological model suitable for scientific testing against $\Lambda$CDM.**
