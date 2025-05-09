# 🌌 Quantum Coherence Cosmology (QCC)
**Full Theory Checkpoint and Reconstruction Log**

> A reproducible, data-anchored replacement to ΛCDM using coherence memory fields derived from the Cosmic Microwave Background.

---

## 📘 Project Overview

This repository contains the full theoretical framework and computational pathway for the **Quantum Coherence Cosmology (QCC)** model. QCC reframes dark matter and dark energy as emergent effects of quantum coherence seeded in the early universe and echoing through spacetime.

This model:
- Extracts coherence structure directly from Planck PCCS 030 GHz CMB data
- Uses wavelet transforms (Daubechies-4) to construct a dynamic scalar field \( \phi(z) \)
- Derives full classical and quantum field equations
- Applies the φ-field to cosmological datasets: Pantheon+, KiDS, DR9Q, BAO, GWTC
- Demonstrates predictive accuracy via RMS residuals and correlation metrics

---

## 📂 Contents

- `qcc_theory.tex` — Full LaTeX document defining the QCC model
- `data/` — Folder for Planck PCCS, KiDS, DR9Q, Pantheon+, and GWTC datasets
- `plots/` — Validation figures: φ(z) overlays, RMS scatter, harmonic coherence
- `scripts/` — Python notebooks and tools for preprocessing, FFT, wavelet generation, and RMS computation

---

## 🧠 Model Highlights

### 🔬 Field Derivation

The scalar coherence field \( \phi(z) \) is derived via:

```math
\phi(z) = \mu(z) - \nu(z)
