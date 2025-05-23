
# qcc_model_v2.py
# Quantum Coherence Cosmology (QCC) Toolkit — V2.0 (CAMB-style)

import numpy as np
from scipy.integrate import cumtrapz
from scipy.interpolate import interp1d

class QCCModel:
    def __init__(self, lambda_phi=50.0, Lambda_phi=1.0, xi=1/6, zmax=2.5, num_points=500):
        self.lambda_phi = lambda_phi
        self.Lambda_phi = Lambda_phi
        self.xi = xi
        self.z = np.linspace(0, zmax, num_points)
        self.phi_vals = self.phi(self.z)
        self.phi_prime_vals = self.phi_prime(self.z)
        self.phi_double_prime_vals = self.phi_double_prime(self.z)

    def phi(self, z):
        return self.Lambda_phi * np.sin(2 * np.pi * z / self.lambda_phi)

    def phi_prime(self, z):
        return self.Lambda_phi * (2 * np.pi / self.lambda_phi) * np.cos(2 * np.pi * z / self.lambda_phi)

    def phi_double_prime(self, z):
        omega = 2 * np.pi / self.lambda_phi
        return -self.Lambda_phi * omega**2 * np.sin(omega * z)

    def xi_plus(self):
        return cumtrapz(self.phi_prime_vals**2, self.z, initial=0)

    def tensor_trace(self):
        return self.phi_prime_vals**2 + self.phi_double_prime_vals**2

    def coherence_pressure(self):
        return self.phi_prime_vals * self.phi_double_prime_vals

    def hawking_decay(self, rho_m):
        return np.exp(-1 / (1 + rho_m))

    def lensing_kernel(self, rho_m=None):
        kernel = self.tensor_trace()
        if rho_m is not None:
            kernel *= self.hawking_decay(rho_m)
        return kernel

    def match_observable(self, z_obs, values=None):
        if values is None:
            values = self.phi_vals
        interp = interp1d(self.z, values, kind='linear', fill_value='extrapolate')
        return interp(z_obs)

    def export_summary(self):
        return {
            "z": self.z.tolist(),
            "phi(z)": self.phi_vals.tolist(),
            "phi'(z)": self.phi_prime_vals.tolist(),
            "xi_plus(z)": self.xi_plus().tolist(),
            "tensor_trace(z)": self.tensor_trace().tolist()
        }
