# Nesvorný et al. (2013): "Inversion of TTV Data to Infer Planetary Parameters."
# Agol et al. (2005): "The Transit Timing Variation Method."
# Holman & Murray (2005): "The Use of Transit Timing to Detect Extrasolar Planets."
import numpy as np

def compute_ttv(masses, orbital_params, transit_index):
    """
    Compute TTV for a given set of masses and orbital parameters.
    Replace this with the actual TTV model for your system.
    """
    # Example: Simple linear model (replace with actual TTV model)
    m1, m2 = masses
    a1, e1, lambda1, a2, e2, lambda2 = orbital_params
    ttv = m1 * a1 + m2 * a2 + e1 * lambda1 + e2 * lambda2  # Example model
    return ttv

def construct_design_matrix(observed_ttvs, masses, orbital_params, delta=1e-6):
    """
    Construct the design matrix using numerical differentiation.
    """
    n_observations = len(observed_ttvs)
    n_parameters = len(masses) + len(orbital_params)
    design_matrix = np.zeros((n_observations, n_parameters))

    for i in range(n_observations):
        for j in range(n_parameters):
            # Perturb the j-th parameter
            perturbed_masses = masses.copy()
            perturbed_orbital_params = orbital_params.copy()
            if j < len(masses):
                perturbed_masses[j] += delta
            else:
                perturbed_orbital_params[j - len(masses)] += delta

            # Compute TTV with perturbed parameters
            ttv_perturbed = compute_ttv(perturbed_masses, perturbed_orbital_params, i)

            # Compute TTV with original parameters
            ttv_original = compute_ttv(masses, orbital_params, i)

            # Numerical derivative
            design_matrix[i, j] = (ttv_perturbed - ttv_original) / delta

    return design_matrix

# Example usage
if __name__ == "__main__":
    # Example observed TTVs (replace with actual data)
    observed_ttvs = np.array([0.1, 0.2, 0.15, 0.3])

    # Example masses and orbital parameters (replace with actual values)
    masses = [1.0, 0.5]  # Masses of the two planets
    orbital_params = [1.0, 0.1, 0.0, 1.5, 0.2, 0.1]  # Orbital parameters: [a1, e1, lambda1, a2, e2, lambda2]

    # Construct design matrix
    design_matrix = construct_design_matrix(observed_ttvs, masses, orbital_params)

    print("Design Matrix:")
    print(design_matrix)
