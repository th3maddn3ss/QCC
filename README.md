# 🚀 Quantum Coherence Cosmology (QCC)

**README and Full Theory Log**
*A reproducible, data-anchored replacement to ΛCDM using coherence memory fields derived from the Cosmic Microwave Background.*

---

## 🔸 Overview

Quantum Coherence Cosmology (QCC) is a cosmological model that replaces dark matter and dark energy with a coherence memory field φ(z) extracted from the Planck CMB PCCS 030 GHz dataset. It explains cosmic structure formation, gravitational lensing, and expansion through quantum coherence evolution, offering predictive power across multiple datasets **without parameter tuning**.

**This repository includes:**

* Full LaTeX documentation of the QCC model
* Cleaned datasets for Pantheon+, KiDS, DR9Q, BAO, and GWTC
* Tools for harmonic extraction, φ-field construction, and RMS validation
* Plots comparing φ(z) forecasts against observed cosmological features
* 🔬 Unified particle model from QCC coherence fields

---

## 📁 Repository Structure

```
QCC Repository/
├── Codebase/                          # Python notebooks and tools for QCC ϕ(z, τ) projection
├── Datasets/                          # All cleaned cosmological datasets (Pantheon+, KiDS, DR9Q, BAO, GWTC)
├── Full_Unified_Field/               # QCC particle-level derivation and coherence field structure
├── Older versions and checkpoints/   # Archived versions like V2.1A and V2.1B
├── Plots/                             # Figures and coherence projection visualizations
├── COM_PCCS_030_R2.04.txt             # Planck 030 GHz compact source catalog
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

### φ(z) Field Derivation

The scalar coherence field is defined as:

```
φ(z) = μ(z) − ν(z)
```

Where:

* μ(z), ν(z): Gaussian wavelet reconstructions of CMB TT peaks and troughs
* Derived from Planck PCCS harmonics via FFT and 720° gimbal smoothing
* Mapped using log-stretched redshift translations

---

## 📜 Canonical Lagrangian

The Lagrangian density for the QCC scalar field φ(z, τ):

```
L_φ = (1/2) g^μν ∂_μ φ ∂_ν φ − V(φ)
```

Where the potential is:

```
V(φ) = (1/2) m² φ² + (λ/4) φ⁴ + α exp(−βz) φ(z, τ)
```

With:

* m: coherence mass scale from harmonic envelope
* λ: self-coupling from structure variance
* α, β: redshift-time echo parameters

---

## 📊 RMS Accuracy

* Pantheon+ RMS: \~0.35
* KiDS RMS: \~0.38–0.48
* DR9Q RMS: \~0.45
* σ₈ RMS (new): \~0.171 with 0.99999 correlation (no tuning)

---

## 🌌 Full\_Unified\_Field/

This folder contains:

* LaTeX derivations of QCC particle generation
* Toroidal coherence plots for leptons, quarks, and baryons
* Validation against PDG particle properties (mass, charge, decay)

**Key Ideas:**

* Leptons and quarks emerge as eigenstates of phase-wrapped φ-ring geometry
* Mass derives from overlap amplitude of constructive coherence nodes
* Charge reflects curvature symmetry and winding number
* Composite particles form from superposed quark toroids in stable interference
* Decay and instability arise from field torsion (e.g., τ lepton, hadrons)

QCC unifies:

```
Cosmic structure + Standard Model particles + Quantum field dynamics
```

— all from a coherence field seeded by CMB memory.

---

## 📌 DOI References

* 📘 **σ₈ Validation (V2.2A)**
  [https://doi.org/10.5281/zenodo.15717400](https://doi.org/10.5281/zenodo.15717400)

* 🌌 **Dynamic QCC (V2.2A)**
  [https://doi.org/10.5281/zenodo.15550647](https://doi.org/10.5281/zenodo.15550647)

* 🧪 **Static QCT (baseline reference)**
  [https://doi.org/10.5281/zenodo.15368572](https://doi.org/10.5281/zenodo.15368572)

---

## 🛠 Development Goals (V2.2B Prep)

* [ ] Package toolkit for CAMB-like use with memory field interactions and particle creation  
* [ ] Build φ(z, τ)-driven structure simulator for large-scale cosmic structure evolution  

## 🔬 Verification & Unification Goals

* [ ] Expand natural particle creation framework via memory field interactions  
* [ ] Validate QCC with recent empirical results, including:  
  - Berry phase effects in levitated nanodiamond NV centers (Purdue)  
  - Thermodynamic cost of information loss (Landauer principle)  
  - New observations from JWST and the Vera C. Rubin Observatory (LSST) 
---

> **QCC is now a predictive, quantized, physically consistent cosmological model suitable for scientific testing against ΛCDM.**

If you encounter any unexpected behavior when reproducing results, testing projections, or verifying φ(z, τ)-based coherence dynamics, I welcome feedback or technical discussion.

Feel free to reach out at: devlav@gmail.com

Even small inconsistencies, data anomalies, or reproducibility questions are appreciated and help improve the robustness of the model.
