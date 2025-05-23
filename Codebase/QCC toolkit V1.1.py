# qcc_model.py
# Quantum Coherence Cosmology (QCC) — Core Computational Toolkit
# For public use in simulations, observable predictions, and QFT-aligned geometry modeling

import numpy as np
from scipy.integrate import cumtrapz
from scipy.interpolate import interp1d

# === Constants ===
lambda_phi = 50.0  # Coherence wavelength (from FFT/MCMC)
xi = 1 / 6  # Conformal Ricci coupling


# === Coherence Field ===
def phi(z, Lambda_phi=1.0):
    """Base coherence field φ(z)."""
    return Lambda_phi * np.sin(2 * np.pi * z / lambda_phi)


def phi_prime(z, Lambda_phi=1.0):
    """First derivative φ′(z)."""
    return Lambda_phi * (2 * np.pi / lambda_phi) * np.cos(2 * np.pi * z / lambda_phi)


def phi_double_prime(z, Lambda_phi=1.0):
    """Second derivative φ″(z)."""
    omega = 2 * np.pi / lambda_phi
    return -Lambda_phi * omega**2 * np.sin(omega * z)


# === Lensing Projections ===
def xi_plus_projection(z, Lambda_phi=1.0):
    """Cumulative φ′²(z) used as lensing analog (∫ φ′² dz)."""
    phi_p = phi_prime(z, Lambda_phi)
    return cumtrapz(phi_p**2, z, initial=0)


def tensor_trace(z, Lambda_phi=1.0):
    """Trace of coherence tensor: φ′² + φ″²."""
    return phi_prime(z, Lambda_phi) ** 2 + phi_double_prime(z, Lambda_phi) ** 2


def coherence_pressure(z, Lambda_phi=1.0):
    """Structure-like observable: φ′(z) * φ″(z)."""
    return phi_prime(z, Lambda_phi) * phi_double_prime(z, Lambda_phi)


# === Decay Models ===
def hawking_decay(rho_m):
    """QFT-compatible decay: φ → φ·exp(–1 / (1 + ρ_m))."""
    return np.exp(-1 / (1 + rho_m))


def damped_phi(z, rho_m=None, Lambda_phi=1.0):
    base = phi(z, Lambda_phi)
    return base * hawking_decay(rho_m) if rho_m is not None else base


# === Example Combined Functions ===
def lensing_kernel(z, Lambda_phi=1.0):
    return xi_plus_projection(z, Lambda_phi)


def full_tensor(z, rho_m=None, Lambda_phi=1.0):
    """Total lensing-like signal from tensor trace, decay-weighted."""
    raw = tensor_trace(z, Lambda_phi)
    if rho_m is not None:
        return raw * hawking_decay(rho_m)
    return raw


# === Interpolation Utilities ===
def match_to_observable(z_model, z_obs, model_vals):
    """Interpolate model values from z_model to z_obs points."""
    f_interp = interp1d(z_model, model_vals, kind="linear", fill_value="extrapolate")
    return f_interp(z_obs)


# === Package Info ===
__version__ = "1.1"
__author__ = "QCC Framework"
__description__ = "Predictive quantum coherence cosmology calculator (φ, φ′, φ″, tensor projection, decay fields)"
