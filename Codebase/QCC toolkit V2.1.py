
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import pywt

class QCCModel:
    def __init__(self, A0=1e-5, z0=1.0, sigma=0.75, lambda_phi=0.9, gamma=0.5):
        self.A0 = A0
        self.z0 = z0
        self.sigma = sigma
        self.lambda_phi = lambda_phi
        self.gamma = gamma
        self.z_span = (0.0, 2.5)
        z_init = self.z0
        self.z_eval = np.linspace(z_init, self.z_span[1], 1000)
        self.kernel_interp = None
        self._solve_field()

    def initial_phi(self, z):
        return self.A0 * np.exp(-((z - self.z0) ** 2) / (2 * self.sigma ** 2)) * np.sin(2 * np.pi * z / self.lambda_phi)

    def dV_dphi(self, phi):
        return phi ** 3  # φ^4 potential derivative

    def phi_ode(self, z, y):
        phi, dphi = y
        ddphi = -self.dV_dphi(phi) - self.gamma * dphi
        return [dphi, ddphi]

    def _solve_field(self):
        # Set initial conditions at z0
        z_init = self.z0
        y0 = [self.initial_phi(z_init), 1e-6]  # small kick to start evolution
        sol = solve_ivp(self.phi_ode, (z_init, self.z_span[1]), y0, t_eval=self.z_eval, method='RK45')

        self.z_vals = sol.t
        self.phi_vals = sol.y[0]
        self.phi_prime = sol.y[1]
        self.phi_double_prime = np.gradient(self.phi_prime, self.z_vals)

        # Normalize using wavelet method
        coeffs = pywt.wavedec(self.phi_vals, wavelet='db4', level=3)
        flat_coeffs = np.concatenate(coeffs)
        lambda_wavelet = np.sqrt(np.mean(flat_coeffs**2))

        # Rescale field and derivatives
        self.phi_vals /= lambda_wavelet
        self.phi_prime /= lambda_wavelet
        self.phi_double_prime /= lambda_wavelet
        self.kernel = self.phi_prime**2 + self.phi_double_prime**2

        # Create interpolator for kernel projection
        self.kernel_interp = interp1d(self.z_vals, self.kernel, fill_value="extrapolate")

    def project_kernel(self, z_array):
        return self.kernel_interp(z_array)

    def get_kernel_data(self):
        return {
            "z": self.z_vals,
            "phi": self.phi_vals,
            "phi_prime": self.phi_prime,
            "phi_double_prime": self.phi_double_prime,
            "kernel": self.kernel
        }
