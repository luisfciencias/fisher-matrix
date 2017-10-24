# definition of cosmological functions

def H(z, params):
    """
    Hubble expansion rate given an input array of redshifts
    and a dictionary of cosmological parameters params
    """
    H0 = params['H0']
    omega_m = params['omega_m']
    # definition of the Hubble parameter
    return H0 * ( omega_m * (1+z)**3 + (1-omega_m))**(0.5)
