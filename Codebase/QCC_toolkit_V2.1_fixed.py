
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import pywt

class QCCModel:
    def __init__(self, A0=1e-5, z0=1.0, sigma=0.75, lambda_phi=0.9, gamma=0.5, mode='dynamic'):
        self.A0 = A0
        self.z0 = z0
        self.sigma = sigma
        self.lambda_phi = lambda_phi
        self.gamma = gamma
        self.mode = mode
        self.z_span = (0.0, 2.5)
        z_init = self.z0
        self.z_eval = np.linspace(self.z_span[0], self.z_span[1], 1000)
        self.kernel_interp = None
    def initial_phi(self, z):
        return self.A0 * np.exp(-((z - self.z0) ** 2) / (2 * self.sigma ** 2)) * np.sin(2 * np.pi * z / self.lambda_phi)

    def dV_dphi(self, phi):
        return phi ** 3  # φ^4 potential derivative

    def phi_ode(self, z, y):
        phi, dphi = y
        ddphi = -self.dV_dphi(phi) - self.gamma * dphi
        return [dphi, ddphi]

    def phi_static(self, z):
        return self.A0 * np.sin(2 * np.pi * z / self.lambda_phi)

    def phi_prime_static(self, z):
        return self.A0 * (2 * np.pi / self.lambda_phi) * np.cos(2 * np.pi * z / self.lambda_phi)

    def phi_double_prime_static(self, z):
        omega = 2 * np.pi / self.lambda_phi
        return -self.A0 * omega**2 * np.sin(omega * z)

    def kernel_static(self, z):
        return self.phi_prime_static(z)**2 + self.phi_double_prime_static(z)**2

    def _solve_field(self):
        if self.mode == 'static':
            self.phi_vals = self.phi_static(self.z_eval)
            self.phi_prime = self.phi_prime_static(self.z_eval)
            self.phi_double_prime = self.phi_double_prime_static(self.z_eval)
            self.kernel = self.kernel_static(self.z_eval)
            self.kernel_interp = None
            return

        # Dynamic mode
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
        self.kernel_interp = None

    def get_kernel_data(self):
        return {
            "z": self.z_eval,
            "phi": self.phi_vals,
            "phi_prime": self.phi_prime,
            "phi_double_prime": self.phi_double_prime,
            "kernel": self.kernel
        }

    def project_kernel(self, z_data):
        z_min = float(np.min(z_data))
        z_max = float(np.max(z_data))
        self.z_span = (z_min, z_max)
        self.z_eval = np.linspace(z_min, z_max, 1000)
        z_init = min(max(z_min, self.z0), z_max - 1e-6)
        self.z_eval = np.linspace(z_init, z_max, 1000)
        y0 = [self.initial_phi(z_init), 1e-6]
        sol = solve_ivp(self.phi_ode, (z_init, z_max), y0, t_eval=self.z_eval, method='RK45')
        self.z_vals = sol.t
        self.phi_vals = sol.y[0]
        self.phi_prime = sol.y[1]
        self.phi_double_prime = np.gradient(self.phi_prime, self.z_vals)
        coeffs = pywt.wavedec(self.phi_vals, wavelet='db4', level=3)
        lambda_phi_wavelet = np.sqrt(np.mean(np.concatenate(coeffs)**2))
        phi_prime_wave_scaled = self.phi_prime / lambda_phi_wavelet
        phi_double_prime_wave_scaled = self.phi_double_prime / lambda_phi_wavelet
        kernel_wave_scaled = phi_prime_wave_scaled**2 + phi_double_prime_wave_scaled**2
        kernel_interp = interp1d(self.z_vals, kernel_wave_scaled, fill_value="extrapolate")
        proj = kernel_interp(z_data)
        return proj / np.max(proj)

    def project_kernel(self, z_data):
        z_min = float(np.min(z_data))
        z_max = float(np.max(z_data))
        self.z_span = (z_min, z_max)
        z_init = min(max(z_min, self.z0), z_max - 1e-6)
        self.z_eval = np.linspace(z_init, z_max, 1000)
        y0 = [self.initial_phi(z_init), 1e-6]
        sol = solve_ivp(self.phi_ode, (z_init, z_max), y0, t_eval=self.z_eval, method='RK45')
        self.z_vals = sol.t
        self.phi_vals = sol.y[0]
        self.phi_prime = sol.y[1]
        self.phi_double_prime = np.gradient(self.phi_prime, self.z_vals)
        coeffs = pywt.wavedec(self.phi_vals, wavelet='db4', level=3)
        lambda_phi_wavelet = np.sqrt(np.mean(np.concatenate(coeffs)**2))
        phi_prime_wave_scaled = self.phi_prime / lambda_phi_wavelet
        phi_double_prime_wave_scaled = self.phi_double_prime / lambda_phi_wavelet
        kernel_wave_scaled = phi_prime_wave_scaled**2 + phi_double_prime_wave_scaled**2
        kernel_wave_scaled[kernel_wave_scaled < 1e-5] = 0.0
        kernel_interp = interp1d(self.z_vals, kernel_wave_scaled, fill_value="extrapolate")
        z_data_clipped = np.clip(z_data, self.z_vals[0], self.z_vals[-1])
        proj = kernel_interp(z_data_clipped)
        return proj / np.max(proj)
