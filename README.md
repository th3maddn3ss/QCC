# 🚀 Quantum Coherence Cosmology (QCC)

**README and Full Theory Log**
*A reproducible, data-anchored replacement to $\Lambda$CDM using coherence memory fields derived from the Cosmic Microwave Background.*

---

## 🔸 Overview

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
├── Codebase/                          # Python notebooks and tools for QCC ϕ(z, τ) projection
├── Datasets/                          # All cleaned cosmological datasets (Pantheon+, KiDS, DR9Q, BAO, GWTC)
├── Full_Unified_Field/               # QCC particle-level derivation and coherence field structure
├── Older versions and checkpoints/   # Archived versions like V2.1A and V2.1B
├── Plots/                             # Figures and coherence projection visualizations
├── COM_PCCS_030_R2.04.txt             # Planck 030 GHz compact source catalog
├── LICENSE                            # BSD 3-Clause License
├── QCC_PrePublish_V2.2A.tex           # Main LaTeX document for final V2.2A release
├── QCC_PrePublish_V2.2A.pdf           # PDF version of the main preprint
├── QCC_V2.2A_Model_Parameters.csv     # Dataset parameters and kernel settings
├── QCC_V2.2A_Physics_Validation.tex   # Microcausality, energy bounds, and causal tests
├── QCC_V2.2A_Reproducibility_Guide.tex # Toolkit usage and step-by-step rebuild instructions
├── QCC_V2.2A_Statistical_Validation.tex # RMS, AIC, BIC, chi-squared, KS evaluation
├── QCC_V2.2A_Unique_Predictions.tex  # QCC-only predictions not explained by ΛCDM
├── README.md                          # Project overview and full theory log
```

---

## 🧠 Model Highlights

### $\phi(z)$ Field Derivation

The scalar coherence field $\phi(z)$ is defined as:

$\phi(z) = \mu(z) - \nu(z)$

Where:

* $\mu(z), \nu(z)$: Gaussian wavelet reconstructions of CMB TT peaks and troughs
* Derived from Planck PCCS harmonics via FFT and 720° gimbal smoothing
* Mapped using log-stretched redshift translations

---

## ✅ Physical Validation

* **GR Limit**:
  $\phi \rightarrow 0 \Rightarrow G_{\mu\nu} = 8\pi G T_{\mu\nu}$

* **Canonical Quantization**:
  $[\phi(z_1), \pi(z_2)] = i\delta(z_1 - z_2)$

* **Energy Conservation**:
  $\nabla^\mu(T_{\mu\nu} + H_{\mu\nu}(\phi)) = 0$

* **Entropy Validity**:
  $S \propto \lambda_{\text{decay}}(\tau - \tau_0)$

* **Microcausality**:
  $[\phi(x), \phi(x')] = 0 \quad \text{for spacelike } (x - x')$

* **Hawking/Unruh Compatibility**:
  $\phi(z, \tau) \text{ decay preserves vacuum physics}$

---

## 📜 Canonical Lagrangian

The Lagrangian density for the QCC scalar field $\phi(z, \tau)$ is:

$\mathcal{L}_{\phi} = \frac{1}{2} g^{\mu\nu} \partial_\mu \phi \, \partial_\nu \phi - V(\phi)$

Where the potential is:

$V(\phi) = \frac{1}{2} m^2 \phi^2 + \frac{\lambda}{4} \phi^4 + \alpha \, e^{-\beta z} \phi(z, \tau)$

With:

* $m$: coherence mass scale from harmonic envelope
* $\lambda$: self-coupling from structure variance
* $\alpha, \beta$: redshift-time echo parameters

---

## 📊 RMS Accuracy

* **Pantheon+ RMS**: \~0.35
* **KiDS RMS**: \~0.38 – 0.48
* **DR9Q RMS**: \~0.45
* Achieved *with slight echo tuning*

---

📌 Current Checkpoint — QCC V3.0

✅ Fully validated  field and dynamic echo kernel

✅ All physical law derivations and QFT compatibility confirmed

✅ Includes unified particle structure model down to leptons and quarks

✅ Full mathematical theory on the structure of base physics established

---

## 🛠 Upcoming Goals

* [ ] Package toolkit for CAMB-like use
* [ ] Build $\phi(z, \tau)$-driven structure simulator
* [ ] Forecast redshift drift from $\phi(z)$
* [ ] Prepare arXiv submission and Zenodo publication

---

## 🌌 Full\_Unified\_Field/

This folder contains:

* LaTeX derivations of QCC particle generation
* Field plots showing toroidal structures for quarks, leptons, and baryons
* Validation against PDG mass/charge for each known Standard Model particle

**Key Ideas:**

* **Leptons and quarks** emerge as eigenstates of phase-wrapped $\phi$ ring geometry.
* **Mass** derives from overlap amplitude of constructive coherence nodes.
* **Charge** reflects curvature symmetry and winding number.
* **Composite particles** (e.g., protons, neutrons) are formed by superposed quark toroids in stable interference.
* **Decay/instability** naturally arise from field torsion, visible in tau and hadron fields.

QCC becomes a unified framework for:

$\text{Cosmic structure} + \text{Standard Model particles} + \text{Quantum field dynamics}$

All derived from a coherence field anchored in the early-universe memory encoded in the CMB.

---

> **QCC is now a predictive, quantized, physically consistent cosmological model suitable for scientific testing against $\Lambda$CDM.**
