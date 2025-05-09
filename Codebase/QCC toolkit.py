# QCC_Test_Toolkit.py
# Toolkit for building, projecting, and testing the QCC φ(z) coherence field with full model logic

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from scipy.stats import pearsonr, spearmanr
import pywt

# -- QCC Scalar Field Components -- #

def coherence_potential(phi, alpha=np.pi, Lambda=1.0):
    """Optional: coherence potential used in Lagrangian."""
    return Lambda * (1 - np.cos(alpha * phi))

def lagrangian_density(phi, dphi_dt):
    """Compute classical scalar field Lagrangian density."""
    return 0.5 * dphi_dt**2 - coherence_potential(phi)

def eom(phi, d2phi_dz2):
    """Return equation-of-motion output at each point."""
    return d2phi_dz2 + np.gradient(coherence_potential(phi), phi)

# -- φ(z) field construction from wavelet components -- #

def build_phi_field(z_array, bursts, wells, sigma=0.00015):
    from scipy.stats import norm
    field = np.zeros_like(z_array)
    for zb in bursts:
        field += norm.pdf(z_array, loc=zb, scale=sigma)
    for zw in wells:
        field -= norm.pdf(z_array, loc=zw, scale=sigma)
    return field

def wavelet_transform(field, wavelet='db4', level=4):
    coeffs = pywt.wavedec(field, wavelet, level=level)
    return pywt.waverec(coeffs, wavelet)[:len(field)]

# -- Green’s function kernel for coherence echo -- #

def generate_kernel(z_grid, phi, lambda_coh=0.2, mode='symmetric'):
    dz_matrix = np.abs(z_grid[:, None] - z_grid[None, :])
    kernel = np.exp(-dz_matrix / lambda_coh) * np.outer(phi, phi)
    if mode == 'causal':
        kernel = np.triu(kernel)
    return kernel

def project_observable(kernel, source_distribution):
    proj = kernel @ source_distribution
    return proj / np.max(proj) if np.max(proj) > 0 else proj

# -- Evaluation against datasets -- #

def compare_projection(observed, projected):
    mask = (observed > 0)
    norm_obs = observed[mask] / np.max(observed[mask])
    norm_proj = projected[mask] / np.max(projected[mask])
    rms = np.sqrt(np.mean((norm_obs - norm_proj) ** 2))
    r, p_r = pearsonr(norm_obs, norm_proj)
    rho, p_s = spearmanr(norm_obs, norm_proj)
    return {
        'RMS': rms,
        'Pearson r': r, 'p (Pearson)': p_r,
        'Spearman ρ': rho, 'p (Spearman)': p_s
    }

# -- Pipeline wrapper for dataset-specific testing -- #

def run_qcc_pipeline(z_grid, bursts, wells, source_hist, lambda_coh=0.2, mode='symmetric'):
    raw_phi = build_phi_field(z_grid, bursts, wells)
    phi_wave = wavelet_transform(raw_phi)
    kernel = generate_kernel(z_grid, phi_wave, lambda_coh=lambda_coh, mode=mode)
    projection = project_observable(kernel, source_hist)
    results = compare_projection(source_hist, projection)
    return {
        'phi(z)': phi_wave,
        'projection': projection,
        'metrics': results,
        'kernel': kernel
    }

# -- Per-dataset derivation wrappers -- #

def get_pantheon_model(z_grid, bursts, wells):
    """Return H(z) from φ(z) for luminosity distance calculations."""
    phi = wavelet_transform(build_phi_field(z_grid, bursts, wells))
    H0 = 70
    H = H0 * (1 + phi)
    return H

def get_dr9q_model(z_grid, bursts, wells):
    """Return φ′²(z) coherence disruption signal for DR9Q."""
    phi = wavelet_transform(build_phi_field(z_grid, bursts, wells))
    dphi_dz = np.gradient(phi, z_grid)
    return dphi_dz**2

def get_kids_lensing_kernel(z_grid, bursts, wells, lambda_coh=0.2):
    """Return coherence kernel to be convolved with shear weighting."""
    phi = wavelet_transform(build_phi_field(z_grid, bursts, wells))
    return generate_kernel(z_grid, phi, lambda_coh)

# Additional models (GWTC, BAO) can be added using similar wrappers
