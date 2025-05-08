# Quantum Coherence Theory (QCT): A Static Structure Model of Dark Matter Encoded in CMB Harmonics

This repository contains all files and data for the structural formulation of **Quantum Coherence Theory (QCT)**, a scalar field framework that models dark matter as quantum coherence memory encoded in the CMB temperature spectrum.

> 🔍 QCT does not propose new particles or modify General Relativity, but instead reconstructs a *static structure model* from CMB harmonic memory. The resulting coherence fields (φ, μ, ν) align with cosmic structure across Pantheon+, KiDS, DR9Q, GWTC, and BAO — without parameter tuning.

---

## 🧾 Contents

### 📄 Preprint
- `QCC Preprint.tex` — LaTeX source of the full theoretical model, with all equations, dataset matching, and figure placements.
- `QCT Structure Theory.pdf` — Compiled PDF of the full paper (same content as `.tex`). Use this for reading or citing.

### 📊 Figures (Field vs Dataset Overlays)
Each image compares a QCT scalar field to its corresponding observable:
- `Pantheon+vsQCCtotal.png`
- `KiDSvsQCCwells.png`
- `DR9QvsQCCwells.png`
- `GWTCvsQCCtotal.png`
- `BAOvsQCCexpandedtotal.png`

All figures include RMS residuals, correlation coefficients, and captions embedded in the LaTeX document.

---

## 📦 Datasets and Cleaning Summary

| Dataset      | Source File | Observable | QCT Field | Cleaning Notes |
|--------------|-------------|------------|-----------|----------------|
| Pantheon+    | `hlsp_ps1cosmo_panstarrs_gpc1_all_multi_v1_snparams.txt` | Distance modulus \( m_B(z) \) | φ(z) | Removed z ≤ 0; kept (z, mB, error) only |
| KiDS         | `KiDS_XIP.txt` | Shear correlation \( \xi_+(\theta) \) | ν(z) | Filtered non-numeric; mapped angle to redshift |
| DR9Q         | `DR9Q.dat` | Quasar histogram | μ(z) | Extracted z column; histogrammed (0.1 < z < 5) |
| GWTC         | `GWTC_Data.txt` | Merger redshift | φ(z) | Removed outliers and invalid z |
| BAO          | `Beutler_etal_DR12COMBINED_BAO_powspec` | \( P(k) \) vs \( k \) | φ(z) | Converted \( k \) to z via \( z \sim 0.3/k \) |

CMB Source:
- `COM_PowerSpect_CMB-TT-full_R3.01.txt` — Planck TT spectrum used to extract φ, μ, ν via harmonic peak and trough mapping.

All cleaning is fully described in the **“Data Cleaning and Preprocessing Rationale”** section of the preprint.

---

## 📘 How to Reproduce

1. Extract CMB peaks and troughs from TT spectrum.
2. Map multipoles to redshift using \( z_i = \frac{1100}{\ell_i + \epsilon} \)
3. Construct φ(z) as:  
   \[
   \phi(z) = \sum A_{\text{peak}} e^{-(z - z_{\text{peak}})^2 / 2\lambda^2} - \sum A_{\text{trough}} e^{-(z - z_{\text{trough}})^2 / 2\lambda^2}
   \]
4. Normalize and overlay against each dataset.
5. Evaluate RMS and correlation (Pearson, Spearman).

Python/NumPy/MATLAB implementations can be built using these equations directly.

---

## 📚 Citation & DOI (Zenodo)

> 📌 Once published on Zenodo, update this section:
```bibtex
@article{lavrisha2025qct,
  title = {Quantum Coherence Theory (QCT): A Static Structure Model of Dark Matter Encoded in CMB Harmonics},
  author = {Devin Lavrisha},
  year = {2025},
  doi = {10.5281/zenodo.XXXXXXX},
  url = {https://doi.org/10.5281/zenodo.XXXXXXX}
}
