import numpy as np

def rejection_sample(pdf, N, lbs, ubs, pdf_max = None):
    """Generate samples from an arbitrary multivariate distribution using Rejection Sampling

    Arguments:
    - pdf: probability density function, takes as input an NxD array, where D is the number of dimensions.
    - N: Number of points to sample
    - lbs: list or array of lower bounds, for each of D dimensions
    - ubs: list or array of lower bounds, for each of D dimensions
    - pdf_max: The maximum value that 'pdf' takes in the interval. If not given, this will be approximated.

    Return:
    - NxD array of samples from 'pdf'
    """
    assert len(lbs) == len(ubs), "Lengths of lower and upper bound arrays must match."
    dims = len(lbs)
    lbs, ubs = np.array(lbs), np.array(ubs)

    if pdf_max is None:
        x_all = np.random.rand(10000, dims)
        pdf_max = np.max(pdf(x_all))

    x = np.empty([0, dims])
    frac = 1. if N > 100 else 100.
    while x.shape[0] < N:
        n_trial = 1 + int((N - x.shape[0])/frac)
        x_trial = np.random.rand(n_trial, dims)
        x_trial = (x_trial * (ubs - lbs)) + lbs

        r = np.random.rand(n_trial) * pdf_max

        comparisons = r < pdf(x_trial).flatten()

        frac = np.sum(comparisons)/n_trial
        if frac == 0:
            frac = 0.01

        x = np.concatenate([x, x_trial[comparisons]], 0)

    return x[:N,:]